# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


class Model(object):
    def __init__(self, data):
        self.__dict__.update(self.defaults())
        self.__dict__.update(data)

    def defaults(self):
        return {
        }

    def __str__(self):
        return '<GWLF-E Model>'

    def values(self):
        return self.__dict__
