#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dan Kolbman'
SITENAME = u'Dan Kolbman'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = None 

# Social widget
SOCIAL = None 

DEFAULT_PAGINATION = False

THEME = 'themes/bootup'

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = {('A', 'About', 'pages/about.html'),
             ('B', 'Contact', 'pages/contact.html'),
             ('C', 'Archives', 'archives.html')}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
