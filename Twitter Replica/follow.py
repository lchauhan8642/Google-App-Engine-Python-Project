from google.appengine.ext import ndb
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from myuser import MyUser
from userinfo import UserInfo
from datetime import datetime
import re
from itertools import combinations


class Follow(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()

        if utilities.userLoggedIn():
            if my_user is None or my_user == '':
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)
            else:
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)

        else:
            renderpage.login(self, utilities.loginUrl(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'follow':

            username = self.request.get('username')

            if username is not None or username != '':
                userinfo_id = username
                userinfo_key = ndb.Key(UserInfo, userinfo_id)
                userin = userinfo_key.get()
                my_user = utilities.userKey()

                my_user.following.append(username)
                my_user.put()

                self.redirect('/')

        elif action == 'unfollow':
            my_user = utilities.userKey()
            user_id = self.request.get('username')
            user_key = ndb.Key(UserInfo, user_id)
            if user_id in my_user.following:
                idx = my_user.following.index(user_id)
                del my_user.following[idx]
                my_user.put()
                self.redirect('/')
