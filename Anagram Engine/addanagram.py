from google.appengine.ext import ndb
import webapp2
import logging
import renderer
import utilities
from anagram import Anagram


class AddAnagram(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        user = utilities.get_my_user()

        if utilities.user_is_logged_in():
            if not utilities.user_exists():
                utilities.add_new_user(utilities.get_user())

            renderer.render_addanagram(self, utilities.get_logout_url(self), user,
                            utilities.get_anagrams_of_user(utilities.get_my_user()))

        else:
            renderer.render_login(self, utilities.get_login_url(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'

        my_user = utilities.get_my_user()
        button = self.request.get('button')
        input_text = utilities.prepare_text_input(self.request.get('value'))
        logging.debug(input_text)
        logging.debug(button)

        if button == 'Add':
            self.add(input_text, my_user)
            self.redirect('/addanagram')


    def add(self, text, my_user):
        logging.debug('Add ' + text)
        if text is not None or text != '':
            anagram_id = utilities.generate_id(text)
            anagram_key = ndb.Key(Anagram, anagram_id)
            anagrams = anagram_key.get()

            if anagrams:
                utilities.add_to_anagram(my_user, text, anagram_key)
            else:
                utilities.add_new_anagram(my_user, text, anagram_id, anagram_key)
