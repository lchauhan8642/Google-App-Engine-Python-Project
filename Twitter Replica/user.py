from google.appengine.ext import ndb
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from userinfo import UserInfo
from myuser import MyUser


class UserSearch(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()
        value = self.request.get('name')
        query = Twitter.query()
        data = query.fetch()

        query1 = UserInfo.query()
        data1 = query1.fetch()

        if utilities.userLoggedIn():
            if my_user is None or my_user == '':
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)
            else:
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.user(self, utilities.logoutUrl(self), my_user, data, data1, value)

        else:
            renderpage.login(self, utilities.loginUrl(self))
