# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tornado.httpclient import HTTPError


class ImproperlyConfigured(Exception):
    """Project is somehow improperly configured"""
    pass


class APIException(HTTPError):
    """Equivalent to ``RequestHandler.HTTPError`` except for in name"""
