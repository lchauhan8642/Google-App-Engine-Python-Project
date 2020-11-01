import os
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

from myuser import MyUser
from address import Address
from datetime import datetime


JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class View(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        query = Address.query()
        data = query.fetch()

        if user == None:
            template_values = {
                'login_url' : users.create_login_url(self.request.uri),
                'addresses': data
            }

            template = JINJA_ENVIRONMENT.get_template('mainpage_guest.html')
            self.response.write(template.render(template_values))
            return

        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        if myuser == None:
            myuser = MyUser(id=user.user_id())
            myuser.put()

        template_values = {
            'logout_url': users.create_logout_url(self.request.uri),
            'addresses': data
        }
        template = JINJA_ENVIRONMENT.get_template('view.html')
        self.response.write(template.render(template_values))

        if self.request.get('button') == 'Cancel':
            self.redirect('/')
