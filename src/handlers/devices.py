# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
from tornado.concurrent import run_on_executor
from tornado.gen import coroutine
from core import hd_wrapper
from core.exceptions import APIException
from core.handlers import APIHandler


class DeviceDetect(APIHandler):
    @run_on_executor
    def detect_device(self, hd, data):
        return hd_wrapper.DetectAPI.detect_device(hd, data)

    @coroutine
    def get(self):
        try:
            data = json.loads(self.request.body.decode("UTF-8"))
        except ValueError:
            raise APIException(400, "JSON is invalid")

        result = yield self.detect_device(self.settings["hd"], data)
        self.write({"device": result})

