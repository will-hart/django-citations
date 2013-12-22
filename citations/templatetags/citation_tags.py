from django import template
import re

from citations.models import Reference as R

register = template.Library()


class CiteNode(template.Node):
    def __init__(self, citation):
        self.citation = citation
        self.citations = [x.replace("\"", "").replace("'", "") for x in citation.split(" ")]

    def render(self, context):
        # create a new reference list if this is the first list of references
        if 'reference_list' not in context:
            context['reference_list'] = []

        ref_ids = []

        # get each reference
        for r in self.citations:
            try:
                ref = R.objects.get(slug=r)
            except R.DoesNotExist:
                raise template.TemplateSyntaxError("Unknown citation: %s" % r)

            if ref in context['reference_list']:
                # find the id of the item in the reference list
                num = context['reference_list'].index(ref) + 1
            else:
                context['reference_list'].append(ref)
                num = len(context['reference_list'])

            if not num in ref_ids:
                ref_ids.append(num)

        if not ref_ids:
            return "[?]"

        return "[" + ", ".join(["<a href='#fn_{0}'>{0}</a>".format(x) for x in sorted(ref_ids)]) + "]"


def do_cite(parser, token):
    """
    Turns a {{cite "reference_slug"}} into a
    """
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, citations = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])

    if not (citations[0] == citations[-1] and citations[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return CiteNode(citations)


@register.inclusion_tag("reference_list.html")
def show_references(reference_list):
    return {'references': reference_list}


@register.inclusion_tag("reference_list.html")
def show_all_references():
    refs = R.objects.all()
    return {'references': refs}


@register.filter
def startswith(value,arg):
    return str(value).startswith(str(arg))


register.tag('cite', do_cite)
