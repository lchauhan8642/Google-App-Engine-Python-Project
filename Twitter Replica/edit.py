from google.appengine.ext import ndb
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from myuser import MyUser
from userinfo import UserInfo
from datetime import datetime


class Edit(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()
        query = UserInfo.query()
        data = query.fetch()

        if utilities.userLoggedIn():
            if my_user is None or my_user == '':
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)
            else:
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.edit(self, utilities.logoutUrl(self), my_user, data)

        else:
            renderpage.login(self, utilities.loginUrl(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'Update':
            first_name = self.request.get('fname')
            last_name = self.request.get('lname')
            username = self.request.get('username')
            about = self.request.get('about')
            dob = self.request.get('dob')

            my_user = utilities.userKey()

            new_data = UserInfo(id=username, username=username, first_name=first_name, last_name=last_name, about=about, dob=datetime.strptime(dob, '%Y-%m-%d'), user_id=my_user.key.id())
            new_data.put()

            self.redirect('/')
