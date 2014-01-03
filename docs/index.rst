================
Django Citations
================

Contents
--------

.. toctree::
   :maxdepth: 2
   
   quickstart
   tags
   advanced

Citations is a simple Django app which lets you use a citations and 
reference lists within your templates. 

 - The source code is available from https://github.com/will-hart/django-citations under an MIT license.  
 - You can find the package on the Python Packing Index https://pypi.python.org/pypi/django-citations/.
 - The latest documentation for the `develop` branch is available from http://django-citations.readthedocs.org/en/latest/

Supported Fields
----------------

The fields currently supported by the django-citations database include:

 - type (currently one of book, electronic journal, journal or website)
 - slug (unique ID for the reference, max 128 characters)
 - author (max 512 characters)
 - title (max 512 characters)
 - year (a number)
 - series (max 512 characters)
 - volume (a number)
 - edition (a number)
 - isbn (up to 17 characters - can include dashes)
 - url (the URL where the resource was accessed online)
 - publisher (max 128 characters)
 - place (place of publishing, max 128 characters)
 - abstract (free text)
 - comments (free text)
 - keywords (free text)
 - accessed (the date the resource was first accessed)

Change Log
----------

**Version 0.4**
 - FIX: HTML anchors for citations
 - ADD: `cite_note` tag
 - ADD: `note` and `show_notes` tags
 - ADD: Consecutive cite tags are merged in templates

**Version 0.3**
 - Improved documentation
 - ADD: new fields to database
 - ADD: bibtex upload function, where `bibtexparser` is installed
 - ADD: `show_all_references` tag for complete bibliography

**Version 0.2.1**
 - FIX tags in README

**Version 0.2**

 - Improved citation database - more fields available
 - Improved reference output (uses a Harvard referencing format)
 
**Version 1.0**

 - Initial version


