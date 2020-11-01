from google.appengine.ext import ndb
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from userinfo import UserInfo
from register import Register
from myuser import MyUser
from edit import Edit
from add import Add
from edittweet import EditTweet
from search import Search
from user import UserSearch
from follow import Follow
from profile import Profile
from uploadhandler import UploadHandler


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()

        query = UserInfo.query()
        data = query.fetch()

        query1 = Twitter.query()
        tweets = query1.fetch()
        user = utilities.currentUser()

        if utilities.userLoggedIn():
            if my_user is None or my_user == '':
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)
            else:
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.main(self, utilities.logoutUrl(self), my_user, user, data, tweets)

        else:
            renderpage.login(self, utilities.loginUrl(self))


app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/register', Register),
        ('/edit', Edit),
        ('/add', Add),
        ('/edittweet', EditTweet),
        ('/search', Search),
        ('/user', UserSearch),
        ('/follow', Follow),
        ('/profile', Profile),
        ('/uploadhandler', UploadHandler),
    ], debug=True)
