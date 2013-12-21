from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render_to_response

import citations.models as reference_models
from django.template import RequestContext

try:
    from citations.forms import BibtexUploadForm
except ImportError:
    pass


class ReferenceAdmin(admin.ModelAdmin):
    change_list_template = 'admin/updated_change_form.html'

    def get_urls(self):
        urls = super(ReferenceAdmin, self).get_urls()

        if 'BibtexUploadForm' in globals():
            new_urls = patterns('',
                url(r'^upload_bibtex/$', self.admin_site.admin_view(self.upload_bibtex_view), name='citations_reference_upload_bibtex')
            )

            return new_urls + urls

        else:
            return urls

    def upload_bibtex_view(self, request):
        if not 'BibtexUploadForm' in globals():
            return render_to_response('admin/unable_to_upload_bibtex.html', {})

        else:
            if request.method == "POST":
                form = BibtexUploadForm(request.POST, request.FILES)
                if form.is_valid():
                    records = form.save()
                    context = {"form": form, "success": True, "records": records}
                    return render_to_response("admin/imported.html", context,
                                              context_instance = RequestContext(request))
            else:
                form = BibtexUploadForm()
                context = {"form": form}
                return render_to_response("admin/imported.html", context,
                                          context_instance=RequestContext(request))


admin.site.register(reference_models.Reference, ReferenceAdmin)
