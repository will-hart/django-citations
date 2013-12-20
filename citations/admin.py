from django.contrib import admin
import citations.models as reference_models


class ReferenceAdmin(admin.ModelAdmin):
    pass


admin.site.register(reference_models.Reference, ReferenceAdmin)
