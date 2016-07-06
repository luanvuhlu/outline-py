#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

from google.appengine.ext import ndb
#from google.appengine.api import users
from properties import UserProperty
from base import NameModel, AddressModel, HistoryModel, CreatorModel

class Role(ndb.Model):
    name=ndb.StringProperty(required=True)
    value=ndb.StringProperty(required=True) #TODO
    description=ndb.StringProperty(required=False)
class User(HistoryModel,AddressModel):
    email=ndb.StringProperty(required=True)
    password=ndb.StringProperty(required=True)  #TODO
    creator=UserProperty(required=False)
    login_type=ndb.IntegerProperty(required=True)   #TODO
    reset_pass_key=ndb.StringProperty(required=False)
    reset_pass_expire=ndb.DateTimeProperty(required=False)
    action_yn=ndb.BooleanProperty(required=True, default=True)
    delete_yn=ndb.BooleanProperty(required=True, default=False)
    block_yn=ndb.BooleanProperty(required=True, default=False)
    block_expire=ndb.DateTimeProperty(required=False)
    avarta_url_full=ndb.StringProperty(required=True)
    avarta_url=ndb.StringProperty(required=True)
    failure_count=ndb.IntegerProperty(required=True, default=0)
    login_again_yn=ndb.BooleanProperty(required=True, default=False)
    date_of_birth=ndb.DateProperty(required=True)
    role=ndb.KeyProperty(kind="Role", required=True)
    family_name=ndb.StringProperty(required=True)
    name=ndb.StringProperty(required=True)
    description=ndb.StringProperty(required=False)
class Page(CreatorModel, HistoryModel):
    title=ndb.StringProperty(required=True)
    url=ndb.StringProperty(required=True)
    description=ndb.StringProperty(required=False)
class Permission(CreatorModel, HistoryModel):
    page=ndb.KeyProperty(kind="Page", required=True)
    role=ndb.KeyProperty(kind="Role", required=False)
    permission=ndb.IntegerProperty(required=True, default=0) #TODO
    description=ndb.StringProperty(required=False)
class Student(User):
    nick_name=ndb.StringProperty(required=False)
    u_class=ndb.KeyProperty(kind="UClass")
class Lecturer(User):
    nick_name=ndb.StringProperty(required=False)
    specialized_study=ndb.KeyProperty(kind="SpecializedStudy", required=False)
