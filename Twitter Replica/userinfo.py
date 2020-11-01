from google.appengine.ext import ndb
from twitter import Twitter


class UserInfo(ndb.Model):
    username = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    about = ndb.StringProperty()
    last_access_date = ndb.DateTimeProperty(auto_now=True)
    dob = ndb.DateProperty()
    user_id = ndb.StringProperty()
