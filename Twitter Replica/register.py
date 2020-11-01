from google.appengine.ext import ndb
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from myuser import MyUser
from userinfo import UserInfo
from datetime import datetime


class Register(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()

        if utilities.userLoggedIn():
            if not utilities.userExist():
                utilities.newUser(utilities.currentUser())

            renderpage.register(self, utilities.logoutUrl(self), my_user)

        else:
            renderpage.login(self, utilities.loginUrl(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'Register':

            first_name = self.request.get('fname')
            last_name = self.request.get('lname')
            username = self.request.get('username')
            about = self.request.get('about')
            dob = self.request.get('dob')

            if username is not None or username != '':
                userinfo_id = username
                userinfo_key = ndb.Key(UserInfo, userinfo_id)
                userin = userinfo_key.get()
                my_user = utilities.userKey()

                new_data = UserInfo(id=userinfo_id, username=username, first_name=first_name, last_name=last_name, about=about, dob=datetime.strptime(dob, '%Y-%m-%d'),user_id=my_user.key.id())
                new_data.put()

                my_user.username = username
                my_user.put()

                self.redirect('/')
