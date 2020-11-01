from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api.images import get_serving_url
from google.appengine.ext import blobstore
import webapp2
import logging
import renderpage
import utilities
from twitter import Twitter
from myuser import MyUser
from uploadhandler import UploadHandler


class Add(webapp2.RequestHandler):
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'
        my_user = utilities.userKey()
        query = Twitter.query()
        data = query.fetch()
        url1 = blobstore.create_upload_url('/uploadhandler')
        if utilities.userLoggedIn():
            if my_user is None or my_user == '':
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.register(self, utilities.logoutUrl(self), my_user)
            else:
                if not utilities.userExist():
                    utilities.newUser(utilities.currentUser())

                renderpage.add(self, utilities.logoutUrl(self), my_user, data, url1)

        else:
            renderpage.login(self, utilities.loginUrl(self))

    def post(self):
        logging.debug("POST")
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'Add':
            my_user = utilities.userKey()
            username = self.request.get('username')
            content = self.request.get('content')
            tags = self.request.get('tags')

            if content is not None or content != '':
                twitter_id = content
                twitter_key = ndb.Key(Twitter, twitter_id)
                tweets = twitter_key.get()
                my_user = utilities.userKey()

                new_data = Twitter(id=twitter_id, username=username, content=content, tags=tags, user_id=my_user.key.id())
                new_data.put()

                my_user.tweets.append(twitter_key)
                my_user.put()

                self.redirect('/')

        elif action == 'Delete':
            my_user = utilities.userKey()
            twitter_id = self.request.get('twitter_id')
            twitter_key = ndb.Key(Twitter, twitter_id)
            if twitter_key in my_user.tweets:
                my_user.tweets.remove(twitter_key)
                my_user.put()
                ndb.Key(Twitter, twitter_id).delete()
                self.redirect('/')
