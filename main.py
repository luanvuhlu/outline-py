#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.content_type="text/plain"
        self.response.write('Xin chào các bạn')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
