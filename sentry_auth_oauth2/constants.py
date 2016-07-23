from __future__ import absolute_import, print_function

from django.conf import settings


AUTHORIZE_URL = getattr(settings, 'OAUTH2_AUTH_URL', '')

ACCESS_TOKEN_URL = getattr(settings, 'OAUTH2_TOKEN_URL', '')

CLIENT_ID = getattr(settings, 'OAUTH2_CLIENT_ID', None)

CLIENT_SECRET = getattr(settings, 'OAUTH2_CLIENT_SECRET', None)

ERR_INVALID_DOMAIN = 'The domain for your auth account (%s) is not allowed to authenticate with this provider.'

ERR_INVALID_RESPONSE = 'Unable to fetch user information from auth.  Please check the log.'

SCOPE = 'email'

DOMAIN_BLOCKLIST = frozenset(getattr(settings, 'OAUTH2_DOMAIN_BLOCKLIST', ['gmail.com']) or [])

DATA_VERSION = '1'
