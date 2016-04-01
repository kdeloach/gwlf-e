# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import json

import numpy


class Model(object):
    def __init__(self, data):
        self.__dict__.update(self.defaults())
        self.__dict__.update(data)

    def defaults(self):
        return {
            'Foo': 'Bar',
        }

    def __str__(self):
        return '<GWLF-E Model>'

    def tojson(self):
        return json.dumps(self.__dict__, cls=NumpyAwareJSONEncoder)


class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
