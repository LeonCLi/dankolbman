#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Kolbman'
SITENAME = 'Dan Kolbman'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

MD_EXTENSIONS = ['codehilite', 'extra']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = None 

# Social widget
SOCIAL = None 

STATIC_PATHS = [ 'DanKolbmanPub.asc' ]

DEFAULT_PAGINATION = False

THEME = 'themes/simple'
THEME_STATIC_DIR = 'simple/static'

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = {('A', 'Contact', 'pages/contact.html'),
             ('B', 'Projects', 'pages/projects.html')}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
