from django import template

from citations.models import Reference as R

register = template.Library()


class CiteNode(template.Node):
    def __init__(self, citations):
        self.citations = citations

    def render(self, context):
        # create a new reference list if this is the first list of references
        if 'reference_list' not in context:
            context['reference_list'] = []

        ref_ids = []
        notes = {}

        # get each reference
        for r in self.citations:
            try:
                ref = R.objects.get(slug=r[0])
            except R.DoesNotExist:
                raise template.TemplateSyntaxError("Unknown citation: %s" % r[0])

            if ref in context['reference_list']:
                # find the id of the item in the reference list
                num = context['reference_list'].index(ref) + 1

            else:
                context['reference_list'].append(ref)
                num = len(context['reference_list'])

            if not num in ref_ids:
                ref_ids.append(num)

            if r[1]:
                if num not in notes.keys():
                    notes[num] = r[1]
                else:
                    notes[num] += ", " + r[1]

        if not ref_ids:
            return "[?]"

        return "[" + "; ".join(["<a href='#fn_{0}'>{0}</a>{1}".format(
            x, "" if x not in notes.keys() else " {0}".format(notes[x])
        ) for x in ref_ids]) + "]"


def parse_citation(tag, contents):
    """
    Parses a citation breaking the id and notes into a tuple
    """
    output = []
    split = contents.split("\" \"")

    if tag == "cite":
        output = [(x.replace("\"", "").replace("'", ""), "") for x in split]
    elif tag == "cite_note":
        output = [(
            split[i].replace("\"", "").replace("'", ""),
            split[i + 1].replace("\"", "").replace("'", "")
        ) for i in range(0, len(split), 2)]

    return output


def do_cite(parser, token):
    """
    Turns a {{cite "reference_slug"}} into an in-text reference
    """

    tag_name, add_citations = token.contents.split(None, 1)
    citations = parse_citation(tag_name, add_citations)

    if parser.tokens:
        while parser.tokens[0].token_type == 2 and len(parser.tokens[0].contents) > 4 and \
                parser.tokens[0].contents[0:4] == 'cite':
            next_token = parser.next_token()
            try:
                tag_name, add_citations = next_token.contents.split(None, 1)
            except ValueError:
                raise template.TemplateSyntaxError("%r tag requires arguments" % next_token.contents.split()[0])

            citations += parse_citation(tag_name, add_citations)

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
register.tag('cite_note', do_cite)
