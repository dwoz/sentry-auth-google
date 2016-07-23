from __future__ import absolute_import

from sentry.auth import register

from .provider import OAuth2Provider

register('oauth2', OAuth2Provider)
