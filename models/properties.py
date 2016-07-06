#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

from google.appengine.ext import ndb

class UserProperty(ndb.KeyProperty):
    def __init__(self, **kwds):
        self.kind="User"
