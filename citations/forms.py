from django.forms import forms

from citations.models import Reference

try:
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.customization import convert_to_unicode
except ImportError:
    pass
else:
    class BibtexUploadForm(forms.Form):
        file = forms.FileField()

        def save(self):

            bibfile = self.cleaned_data['file'].file
            bp = BibTexParser(bibfile, customization=convert_to_unicode)


            good = 0
            bad = 0
            results = []

            for item in bp.get_entry_list():
                # find the common keys
                keys = set(Reference._meta.get_all_field_names()).intersection(item.keys())

                # populate the common fields
                r = Reference()
                for k in keys:

                    if k == 'id':
                        setattr(r, 'slug', item[k])
                    else:
                        setattr(r, k, item[k])

                try:
                    r.save()
                except Exception as e:
                    bad += 1
                    results.append("![{0}]: {1}".format(r.slug, e.message))
                else:
                    good += 1
                    results.append("[{0}]: {1}".format(r.slug, r.title))

            return good, bad, results
