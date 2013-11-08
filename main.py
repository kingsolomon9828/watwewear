import httplib2
import logging
import os
import cgi
import pickle
import urllib2
import httplib
import json
import mimetypes

#from apiclient.discovery import build
#from oauth2client.appengine import oauth2decorator_from_clientsecrets
#from oauth2client.client import AccessTokenRefreshError
#from oauth2client.client import Credentials
from apiclient.http import MediaFileUpload
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import db
import webapp2
import jinja2
import oauth2client.appengine
import oauth2client.client


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
    extensions=['jinja2.ext.autoescape'])
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        template = JINJA_ENVIRONMENT.get_template('')
        self.response.write(template.render({'': }))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)