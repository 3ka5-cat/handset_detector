# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from tornado.web import RequestHandler


class APIHandler(RequestHandler):

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