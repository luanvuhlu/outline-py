#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"

import sys
sys.path.insert(1, '/home/luanvv/PycharmProjects/outline-py')
sys.path.insert(1, '/home/luanvv/PycharmProjects/outline-py/models')
sys.path.insert(1, '/usr/lib/google_appengine/')
sys.path.insert(1, '/usr/lib/google_appengine/lib/yaml/lib/')
sys.path.insert(1, '/home/luanvv/PycharmProjects/outline-py/lib')
import unittest
import webapp2
import webtest
from main import MainHandler
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from user import User, Role

class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a WSGI application
        app = webapp2.WSGIApplication([('/', MainHandler)])
        # Wrap the app with WebTest's TestApp
        self.testapp = webtest.TestApp(app)
        # Test the handler.
    def testHelloWorldHandler(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.normal_body, 'Xin chào các bạn')
        self.assertEqual(response.content_type, 'text/plain')
class DatastoreTestCase(unittest.TestCase):
    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        # Clear ndb's in-context cache between tests.
        # This prevents data from leaking between tests.
        # Alternatively, you could disable caching by
        # using ndb.get_context().set_cache_policy(False)
        ndb.get_context().clear_cache()
    def tearDown(self):
        self.testbed.deactivate()
    def testInsertEntity(self):
        role=Role(name="Admin", value="AD")
        role.put()
        print(Role.query().fetch())
        self.assertEqual(1, len(Role.query().fetch()))

if __name__ == '__main__':
    unittest.main()
