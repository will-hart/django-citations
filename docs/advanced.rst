========================
Advanced Tips and Tricks
========================

Importing References from Bibtex
--------------------------------

If you have the package `bibtexparser` installed then you will have access in the admin
panel to an "Upload Bibtex" button.  This feature will upload a bibtex file, scan it for 
fields that django-citations supports and save new records.

The `bibtexparser` package is provided under the LGPL.


Including a complete bibliography
---------------------------------

As of version 0.3, you can include a complete bibliography by using the `show_all_references`
template tag.  This looks like the following::

    {% load citation_tags %}

    ...
    
    {% show_all_references %}


Loading templates from database
-------------------------------

Sometimes you want to load the text including citations from the database.  
In this case, you can add a property to your model which builds the text into
a template.  This could look something like this::

    from django.template import Template, Context

    class MyModel(models.Model):
        body = models.TextField()
        
        def get_rendered_body(self):
            tpl = Template("{% load citation_tags %}" + self.body + "{% show_references reference_list %}")
            ctx = Context()
            return tpl.render(ctx)
            
        rendered_body = property(get_rendered_body)
        
This will include the text as well as a reference list at the bottom.  Note that
as the `reference_list` variable is located in the local template context then it
is not available in the global template context - therefore you must include the
reference list in the same template as the citations.