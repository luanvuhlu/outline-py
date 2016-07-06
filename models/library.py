#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

from google.appengine.ext import ndb
from base import NameModel, AddressModel, HistoryModel, CreatorModel

class Library(NameModel, HistoryModel, CreatorModel):
    university=ndb.KeyProperty(kind="University", required=False)

class LearningResourceType(HistoryModel, CreatorModel):
    name=ndb.StringProperty(required=True)

class LearningResource(HistoryModel, CreatorModel):
    name=ndb.StringProperty(required=True)
    library=ndb.KeyProperty(kind="Library", required=True)
    resource_type=ndb.KeyProperty(kind="LearningResourceType", required=True)
    avaiable_yn=ndb.BooleanProperty(required=True, default=True)
    buy_yn=ndb.BooleanProperty(required=True, default=False)
    buy_place=ndb.StringProperty(required=False)
    borrow_yn=ndb.BooleanProperty(required=True, default=True)
    borrow_place=ndb.StringProperty(required=False)

