#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Thiago Sem W'
SITENAME = 'Codetutor'
SITEURL = ''

PATH = 'content'
THEME = 'themes/minimalist'

TIMEZONE = 'America/Sao_Paulo'
LOAD_CONTENT_CACHE = False
DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('stack-overflow', 'https://pt.stackoverflow.com/users/88315/thiagoluizs'),
    ('github', 'https://github.com/ThiaguinhoLS/'),
    ('twitter', 'https://twitter.com/ThiaguinhoLS3'),
    ('facebook', 'thiagoluizs@yahoo.com'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True