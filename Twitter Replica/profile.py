from google.appengine.ext import ndb
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from userinfo import UserInfo
from myuser import MyUser


class Profile(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()

        query = Twitter.query()
        tweets = query.fetch()

        query1 = UserInfo.query()
        userinfo = query1.fetch()

        if utilities.userLoggedIn():
            if my_user is None or my_user == '':
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)
            else:
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.profile(self, utilities.logoutUrl(self), my_user, tweets, userinfo)

        else:
            renderpage.login(self, utilities.loginUrl(self))
