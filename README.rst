================
Django Citations
================

Citations is a simple Django app which lets you use a citations and 
reference lists within your templates. 

The source code is available from https://github.com/will-hart/django-citations
under an MIT license

Quick start
-----------

1. Add "citations" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'citations',
    )

2. Run `python manage.py migrate` to create the polls models.


Usage
-----

You can use the admin panel to create references for your site.  These can
have a range of details including ISBN, URLs, titles, etc. Each reference 
must have a unique slug.  This is how we will refer to the reference when we
cite it within a template.

To refer to a reference in your database, you first need to load the tags in
your template::

    {% load citation_tags %}

You can then do the following in your template where you want the reference to
appear::

    {% cite "my_reference_slug" %}
    
You can refer to multiple references at a time by just adding new slugs separated by spaces.
Note that quotation marks are required around the slugs, and slug names should not contain 
spaces::

    {% cite "my_first_reference_slug" "my_second_reference_slug" %}
    
If you attempt to reference a work that is not in your reference list a TemplateSyntaxError
will be raised showing the offending reference slug.  

The references will be included in text as numbers - e.g. `[1]`, or `[1, 2]` for multiple
references.  Reference objects will also be placed in the `reference_list` variable of the
template's context.  

A reference list can be included at the bottom of the document::

    {% show_references reference_list %}
    
Change Log
----------

**Version 0.2**

 - Improved citation database - more fields available
 - Improved reference output (uses a Harvard referencing format)
 
**Version 1.0**

Initial version