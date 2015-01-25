# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = "Tweetab"
response.subtitle = "Housing.com-Hiring Challenge-Round 2:Twitter Clone"
response.menu = [
    (T('Tweet Dash'), False, URL('default','home')),
    (T('Profile'), False, URL('default','wall')),
    (T('Lookup'), False, URL('default','search')),
    ]
