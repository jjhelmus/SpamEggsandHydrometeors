#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Jonathan J. Helmus'
SITENAME = u'Spam, Eggs and Hydrometeors'
SITESUBTITLE = u'A blog on Python and Atmospheric science'
SITEURL = ''

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('About the author', 'http://nmrglue.com/jhelmus')]
NEWEST_FIRST_ARCHIVES = False


# github include setting
GITHUB_USER = 'jjhelmus'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = os.path.join(os.environ.get('HOME'),
                     'projects/blog/pelican-octopress-theme/')
PLUGIN_PATH = os.path.join(os.environ.get('HOME'),
                           'projects/blog/pelican-plugins')
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']


# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
#
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Sharing
TWITTER_USER = ''
GOOGLE_PLUS_USER = ''
GOOGLE_PLUS_ONE = False
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = False
TWITTER_LATEST_TWEETS = False
TWITTER_FOLLOW_BUTTON = False
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True
