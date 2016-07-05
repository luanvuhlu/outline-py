#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__="luanvv"
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Xin chào các bạn 2 3 4 !')
        self.response.write('<br />Hello')
        self.response.write('<br />Good bye abc')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
