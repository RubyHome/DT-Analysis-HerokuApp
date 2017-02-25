import os
from .common import *




# Use Whitenoise to serve static files
# See: https://whitenoise.readthedocs.io/
WHITENOISE_MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE


ALLOWED_HOSTS = ['*']