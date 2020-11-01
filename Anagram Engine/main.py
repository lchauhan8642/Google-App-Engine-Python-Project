from google.appengine.ext import ndb
import webapp2
import os
import logging
import renderer
import utilities
from anagram import Anagram
from addanagram import AddAnagram
from search import Search
from upload import Upload
from subanagram import SubAnagram


class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        user = utilities.get_my_user()

        if utilities.user_is_logged_in():
            if not utilities.user_exists():
                utilities.add_new_user(utilities.get_user())

            renderer.render_main(self, utilities.get_logout_url(self), user,
                                 utilities.get_anagrams_of_user(utilities.get_my_user()))

        else:
            renderer.render_login(self, utilities.get_login_url(self))


app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/addanagram', AddAnagram),
        ('/search', Search),
        ('/upload', Upload),
        ('/subanagram', SubAnagram),
    ], debug=True)
