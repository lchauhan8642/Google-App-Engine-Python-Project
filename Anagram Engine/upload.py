from google.appengine.ext import ndb
import webapp2
import logging
import renderer
import utilities
from anagram import Anagram
from addanagram import AddAnagram
import re
from myuser import MyUser
from itertools import combinations


class Upload(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'

        if utilities.user_is_logged_in():
            if not utilities.user_exists():
                utilities.add_new_user(utilities.get_user())

            renderer.render_upload(self, utilities.get_logout_url(self),
                                 utilities.get_anagrams_of_user(utilities.get_my_user()))

        else:
            renderer.render_login(self, utilities.get_login_url(self))


    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'

        my_user = utilities.get_my_user()
        button = self.request.get('button')
        file = self.request.get('file')
        out = []
        buff = []
        with open(file, 'r') as file:
            dictionaryWord = "%s" % (file.read())
            for c in dictionaryWord:
                if c == '\n':
                    out.append(''.join(buff))
                    buff = []
                else:
                    buff.append(c)
            else:
                if buff:
                    out.append(''.join(buff))
        print(out)
        for i in out:
            dictionaryWord = i
            lowercaseWord = dictionaryWord

            input_text = utilities.prepare_text_input(lowercaseWord)
            logging.debug(input_text)
            logging.debug(button)

            if button == 'Upload':
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
