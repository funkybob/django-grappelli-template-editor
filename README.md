django-grappelli-template-editor
================================

Allows you to edit templates through an extra Grappelli dashboard page


Installation
------------

Add to INSTALLED_APPS

Into your root urls, before admin, insert the line:

    (r'^admin/templates/', include('grappeli_te.urls')),


Usage
-----

Visting that URL will present you with a page with a list of templates found
in the first entry of settings.TEMPLATE_DIRS, and an edit box.  Double click a
template to load, and edit away.

