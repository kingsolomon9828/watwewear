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
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                          (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
                        
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render({'greeting': greeting}))

application = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)