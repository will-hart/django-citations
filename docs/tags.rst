=============
Template tags
=============

cite
----

    {% cite "slugs" ... %}
    
Use the cite template to cite a reference in the body of the text.  Any number
of reference slugs can be provided as space separated values inside quotation
marks.  A `reference_list` variable will be added to the template context which
contains all the works cited in the article to date.

show_references
---------------

    {% show_references list_of_reference_objects %}
    
Displays a reference list of all the objects passed in the `list_of_reference_objects`
variable.

show_all_references
-------------------

    {% show_all_references %}
    
Shows a reference list including all references in the database, sorted alphabetically 
by author.

