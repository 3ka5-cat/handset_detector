# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tornado.web import RequestHandler
from .exceptions import ImproperlyConfigured


class APIHandler(RequestHandler):
    executor = None

    def initialize(self):
        self.executor = self.settings.get("executor")
        if "hd" not in self.settings:
            raise ImproperlyConfigured("HandsetDetection is missed from settings")

    def write(self, data, **kwargs):
        result = dict(success=True, data=data)
        super(APIHandler, self).write(result)
    
    def write_error(self, status_code=None, **kwargs):
        result = dict(success=False)
        exception = kwargs.get("exc_info")
        if exception:
            result["data"] = str(exception[1])
        super(APIHandler, self).write(result)
        self.finish()
