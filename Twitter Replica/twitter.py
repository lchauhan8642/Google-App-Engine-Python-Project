from google.appengine.ext import ndb


class Twitter(ndb.Model):
    user_id = ndb.StringProperty()
    username = ndb.StringProperty()
    content = ndb.StringProperty()
    tweet_date = ndb.DateTimeProperty(auto_now=True)
    image_name = ndb.StringProperty()
    blobstore = ndb.BlobKeyProperty()
    image_path = ndb.StringProperty()
