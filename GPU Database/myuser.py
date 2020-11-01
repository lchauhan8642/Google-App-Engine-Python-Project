from google.appengine.ext import ndb
from address import Address


class MyUser(ndb.Model):
    username = ndb.StringProperty()
    addresses = ndb.StructuredProperty(Address, repeated=True)
