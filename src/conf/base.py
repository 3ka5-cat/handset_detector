# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import tornado
from tornado.options import define

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

settings = {
}
