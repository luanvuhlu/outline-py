#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

from google.appengine.ext import ndb
from google.appengine.api import users
from base import NameModel, AddressModel, HistoryModel, CreatorModel

class University(NameModel, AddressModel, HistoryModel, CreatorModel):
    founding=ndb.DateTimeProperty(required=False)

class SpecializedStudy(NameModel, CreatorModel, HistoryModel):
    address=ndb.StringProperty(required=False)
    university=ndb.KeyProperty(kind="University", required=True)

class Course(NameModel, CreatorModel, HistoryModel):
    university=ndb.KeyProperty(kind="University", required=True)
    current_yn=ndb.BooleanProperty(required=True, default=True)

class UClass(NameModel, HistoryModel, CreatorModel):
    course=ndb.KeyProperty(kind="Course", required=True)
    specialized_study=ndb.KeyProperty(kind="SpecializedStudy", required=False)
    description=ndb.StringProperty(required=False)

class Subject(NameModel, HistoryModel, CreatorModel):
    specialized_study=ndb.KeyProperty(kind="SpecializedStudy", required=True)
    credit=ndb.IntegerProperty(required=True, default=2)
    description=ndb.StringProperty(required=False)

class Scholastic(HistoryModel, CreatorModel):
    name=ndb.StringProperty(required=True)


