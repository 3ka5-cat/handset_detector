# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from concurrent.futures import ThreadPoolExecutor
from handsetdetection.HD4 import HandsetDetection

import tornado
from tornado.options import define

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

executor = ThreadPoolExecutor(max_workers=16)

# HandsetDetection is basically just a storage with read methods,
# so we will init and store in settings, just like any other db
hd_config = {
    "use_local": True,
    "filesdir": "../",
}
hd = HandsetDetection()
hd.setConfig({"config": hd_config})

settings = {
    "hd": hd,
    "executor": executor,
}
