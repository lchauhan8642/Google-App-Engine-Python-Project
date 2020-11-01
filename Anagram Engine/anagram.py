from google.appengine.ext import ndb


class Anagram(ndb.Model):
    sorted_word = ndb.StringProperty()
    length = ndb.IntegerProperty()
    user_id = ndb.StringProperty()
    words = ndb.StringProperty(repeated=True)
    sub_anagram = ndb.StringProperty(repeated=True)
