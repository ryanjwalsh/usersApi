# main.py

import webapp2
import os

# This initializes the jinja2 environment
# THIS IS GOING TO BE THE SAME FOR EVERY APP YOU BUILD
# jinja2.Environment is a CONSTRUCTOR
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
	pass

#  the app configuration section
app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
    ],
    debug = True
)
