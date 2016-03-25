# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .vendors import VendorListHandler, VendorModelListHandler, VendorModelHandler
from .devices import DeviceDetect

routes = [
    (r"/vendors/?", VendorListHandler),
    (r"/vendors/([A-Za-z0-9]+)/models/?", VendorModelListHandler),
    (r"/vendors/([A-Za-z0-9]+)/models/([A-Za-z0-9]+)/?", VendorModelHandler),
    (r"/device/?", DeviceDetect),
]
