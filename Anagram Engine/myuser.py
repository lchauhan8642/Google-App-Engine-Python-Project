from google.appengine.ext import ndb
from anagram import Anagram


class MyUser(ndb.Model):
    anagrams = ndb.KeyProperty(kind=Anagram, repeated=True)
    anagram_count = ndb.IntegerProperty(default=0)
    words_count = ndb.IntegerProperty(default=0)
