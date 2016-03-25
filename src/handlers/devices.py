# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

from core.handlers import APIHandler


class DeviceDetect(APIHandler):
    def get(self):
        query = json.loads(self.request.body.decode("UTF-8"))
        mandatory_fields = ["width", "height"]
        missed_fields = []
        for field in mandatory_fields:
            if field not in query:
                missed_fields.append(field)
        if missed_fields:
            raise KeyError("Fields are mandatory: {}".format(",".join(missed_fields)))

        result = {"query": query,
                  "device": {"name": "N80"}}
        self.write(result)
