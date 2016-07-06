#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

from google.appengine.ext import ndb
from google.appengine.ext.ndb.polymodel import PolyModel
from properties import UserProperty
class NameModel(PolyModel):
    name=ndb.StringProperty(required=True)
    name_abbr=ndb.StringProperty(required=False)
class AddressModel(PolyModel):
    address_1=ndb.StringProperty(required=False)
    address_2=ndb.StringProperty(required=False)
    address_3=ndb.StringProperty(required=False)
    city=ndb.StringProperty(required=True)
class HistoryModel(PolyModel):
    create_time=ndb.DateTimeProperty(auto_now_add=True, required=True)
    update_time=ndb.DateTimeProperty(required=False)
class CreatorModel(PolyModel):
    user=UserProperty(required=True)
