# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tornado.web import RequestHandler


class APIHandler(RequestHandler):
    
    def write_error(self, status_code=None, **kwargs):
        message = {"status": "error"}
        exception = kwargs.get("exc_info")
        if exception:
            message["data"] = str(exception[1])
        self.write(message)
        self.finish()