#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

from google.appengine.ext import ndb
from google.appengine.api import users

class Role(ndb.Model):
    name=ndb.StringProperty(required=True)
    value=ndb.StringProperty(required=True) #TODO
    description=ndb.StringProperty(required=False)
class User(ndb.Model):
    email=ndb.EmailProperty(required=True)
    password=ndb.PasswordProperty(required=True)
    create_time=ndb.DateTimeProperty(auto_now_add=True, required=True)
    update_time=ndb.DateTimeProperty(required=False)
    creator=ndb.KeyProperty(kind="User")
    login_type=ndb.IntegerProperty(required=True)   #TODO
    reset_pass_key=ndb.StringProperty(required=False)
    reset_pass_expire=ndb.DateTimeProperty(required=False)
    action_yn=ndb.BooleanProperty(required=True, default=True)
    delete_yn=ndb.BooleanProperty(required=True, default=False)
    block_yn=ndb.BooleanProperty(required=True, default=False)

class Permission(ndb.Model):
    pass
