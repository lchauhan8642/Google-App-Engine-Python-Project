from google.appengine.ext import ndb
import webapp2
import logging
import renderer
import utilities
from anagram import Anagram


class Search(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'

        if utilities.user_is_logged_in():
            if not utilities.user_exists():
                utilities.add_new_user(utilities.get_user())

            renderer.render_searchtext(self, utilities.get_logout_url(self),
                                       utilities.generate_id(self.request.get('value')),
                                       utilities.prepare_text_input(self.request.get('value')),
                                       utilities.get_anagrams_of_user(utilities.get_my_user()))

        else:
            renderer.render_login(self, utilities.get_login_url(self))
