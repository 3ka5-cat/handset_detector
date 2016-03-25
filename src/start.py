#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import tornado.ioloop
from tornado.options import options
from tornado.web import Application

from conf import settings
from handlers import urls


def main():
    application = Application(handlers=urls.routes, settings=settings)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
