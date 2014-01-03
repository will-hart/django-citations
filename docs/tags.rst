=============
Template tags
=============

cite
----

    {% cite "slugs" ... %}
    
Use the cite tag to cite a reference in the body of the text.  Any number
of reference slugs can be provided as space separated values inside quotation
marks.  A `reference_list` variable will be added to the template context which
contains all the works cited in the article to date.

cite_note
---------

    {% cite_note "slug" "note" ... %}

Use the cite_note tag to cite a reference in the body of the text with some supporting
notes.  For instance "[1 p20]" would be achieved by using `{% cite_note "slug" "p20" %}.  
As with the `cite` tag, a series of reference-note pairs can be provided to reference 
multiple works within a single tag.  A `reference_list` variable will be added to the 
template context which contains all the works cited in the article to date.

.. note:: To quote multiple works in one reference block (e.g. [1; 2; 3]) you can either provide multiple slugs inside the tag, or use multiple tags with no separating characters or white space.  Django-citations will search for consecutive tags and merge them.

note
----

    {% note "This is a note" %}
    
Adds an in text note, marked as, for instance marked in text as  "[Note a]", and populates
a `note_list` variable in the current context.  Use the `show_notes` tag to display the 
note list.  Make sure the note is within quotation marks.

show_notes
----------

    {% show_notes list_of_notes %}

Displays a list of all the note strings passed in the `list_of_notes` variable.

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

