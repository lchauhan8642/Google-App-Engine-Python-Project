from google.appengine.ext import ndb
from twitter import Twitter


class MyUser(ndb.Model):
    tweets = ndb.KeyProperty(kind=Twitter, repeated=True)
    username = ndb.StringProperty()
    follower = ndb.StringProperty(repeated=True)
    following = ndb.StringProperty(repeated=True)
    follower_count = ndb.IntegerProperty()
    following_count = ndb.IntegerProperty()
