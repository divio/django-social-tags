# django-social-tags
This tool is supposed to make it easier to handle the meta attributes that are often needed for social networks, for example OpenGraph, which is used by Facebook and Google+.

## Supported Networks
* Facebook (OpenGraph)
* Google (OpenGraph)
* Twitter (Cards API)

## Installation
The installation is a bit of a pain in the ass.

1. Install the `django-social-tags` as you would everything else (e.g. `pip install django-social-tags`)
2. add `'social_tags'` to your `INSTALLED_APPS` in your `settings.py`
3. insert `'social_tags.context_processors.social'` into `TEMPLATE_CONTEXT_PROCESSORS`
4. in your base template (it has to be the base template):

    1. add `social_meta` and `sekizai_tags` to your `{% load %}` tag.
    2. add the line 
        `{% with_data 'social_tags' as data %}{% render_meta_tags data %}{% end_with_data %}`
        inside the `<head>` tag.

I realize the last step is still pretty ugly, working on that.

## Usage
The values for the tags are collected on three levels (sorted by priority top to bottom):

1. Template/Request
2. Context
3. Preset defaults

### Defaults
For most attributes there is a setting in the form of `SOCIAL_TAGS_DEFAULT_ATTRIBUTE`.

### Context
To modify some value out of a view, simply modify the `context['social_tags']` dictionary.

### Template
After loading the `social_meta` tag library, you can set attributes via `{% set_tag attribute value %}`