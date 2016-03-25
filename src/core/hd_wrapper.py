# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class HandsetDetectionAPI(object):
    @classmethod
    def _handle_output(cls, key, output):
        if output["status"] == 0:
            return output[key]
        elif output["status"] == 301:
            return []
        else:
            raise Exception("Detection library internal error")


class VendorsAPI(HandsetDetectionAPI):
    @classmethod
    def vendor_list(cls, hd):
        result = hd.deviceVendors()
        return cls._handle_output(key="vendor", output=result)

    @classmethod
    def vendor_model_list(cls, hd, vendor):
        result = hd.deviceModels(vendorName=vendor)
        return cls._handle_output(key="model", output=result)

    @classmethod
    def vendor_model(cls, hd, vendor, model):
        result = hd.deviceView(vendor=vendor, model=model)
        return cls._handle_output(key="device", output=result)


class DetectAPI(HandsetDetectionAPI):
    @classmethod
    def detect_device(cls, hd, data):
        result = hd.deviceDetect(data)
        return cls._handle_output(key="hd_specs", output=result)

