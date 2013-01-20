# -*- coding: utf-8 -*-
from social_tags import settings


DEFAULT_SETTINGS = {
    'type': settings.DEFAULT_TYPE,
    'image': settings.DEFAULT_IMAGE,
    'locales': settings.DEFAULT_LOCALES,
    'description': settings.DEFAULT_DESCRIPTION,
    'twitter': {
        'card': 'summary',
        'site_id': settings.DEFAULT_TWITTER_SITE_ID,
        'creator_id': settings.DEFAULT_TWITTER_CREATOR_ID,
    }
}

