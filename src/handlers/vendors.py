# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from tornado.concurrent import run_on_executor
from tornado.gen import coroutine

from core import hd_wrapper
from core.handlers import APIHandler


class VendorListHandler(APIHandler):

    @run_on_executor
    def get_vendors(self, hd):
        return hd_wrapper.VendorsAPI.vendor_list(hd)

    @coroutine
    def get(self):
        result = yield self.get_vendors(self.settings["hd"])
        self.write({"vendors": result})


class VendorModelListHandler(APIHandler):

    @run_on_executor
    def get_vendor_model_list(self, hd, vendor):
        return hd_wrapper.VendorsAPI.vendor_model_list(hd, vendor)

    @coroutine
    def get(self, vendor):
        result = yield self.get_vendor_model_list(self.settings["hd"], vendor)
        self.write({"models": result})


class VendorModelHandler(APIHandler):

    @run_on_executor
    def get_vendor_model(self, hd, vendor, model):
        return hd_wrapper.VendorsAPI.vendor_model(hd, vendor, model)

    @coroutine
    def get(self, vendor, model):
        result = yield self.get_vendor_model(self.settings["hd"], vendor, model)
        self.write({"model": result})
