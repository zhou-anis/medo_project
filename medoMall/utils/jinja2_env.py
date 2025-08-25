from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

def jinja_environment(**kwargs):
    env = Environment(**kwargs)

    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    return env