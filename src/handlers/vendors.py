# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .base import APIHandler


class VendorListHandler(APIHandler):
    def get(self):
        result = dict(success=True,
                      data={"vendors": [
                          {"name": "Nokia"},
                          {"name": "Siemens"}
                      ]})
        self.write(result)


class VendorModelListHandler(APIHandler):
    def get(self, vendor):
        result = dict(success=True,
                      data={"models": [
                          {"name": "N80"},
                          {"name": "N90"}
                      ]})
        self.write(result)


class VendorModelHandler(APIHandler):
    def get(self, vendor, model):
        result = dict(success=True,
                      data={"model": {"name": "N80"}})
        self.write(result)
