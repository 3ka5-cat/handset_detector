# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from tornado.gen import coroutine

from core.exceptions import ImproperlyConfigured
from .base import APIHandler


class VendorListHandler(APIHandler):
    executor = ThreadPoolExecutor(max_workers=4)

    @run_on_executor
    def get_vendors(self, hd):
        result = hd.deviceVendors()
        if result["status"] == 0:
            vendors = result["vendor"]
        elif result["status"] == 301:
            vendors = []
        else:
            raise Exception("Internal error")

        return vendors

    @coroutine
    def get(self):
        if "hd" not in self.settings:
            raise ImproperlyConfigured("HandsetDetection is missed from settings")

        result = yield self.get_vendors(hd=self.settings["hd"])

        self.write({"vendors": result})


class VendorModelListHandler(APIHandler):
    def get(self, vendor):
        result = {"models": [
            {"name": "N80"},
            {"name": "N90"}
        ]}
        self.write(result)


class VendorModelHandler(APIHandler):
    def get(self, vendor, model):
        result = {"model": {"name": "N80"}}
        self.write(result)
