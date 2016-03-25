# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tornado.web import RequestHandler
from .exceptions import ImproperlyConfigured, APIException


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
        exception_info = kwargs.get("exc_info")
        if exception_info:
            exception = exception_info[1]
            if not isinstance(exception, APIException):
                self.clear()
                self.set_status(500)
                result["data"] = "Internal error"
            else:
                self.set_status(exception.code)
                result["data"] = str(exception)
        super(APIHandler, self).write(result)
        self.finish()
