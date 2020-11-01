from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from twitter import Twitter
from userinfo import UserInfo
import logging
import re
from itertools import combinations
from datetime import datetime


def loginUrl(main_page):
    return users.create_login_url(main_page.request.uri)


def logoutUrl(main_page):
    return users.create_logout_url(main_page.request.uri)


def currentUser():
    return users.get_current_user()


def userKey():
    user = currentUser()
    if user:
        my_user_key = ndb.Key(MyUser, user.user_id())
        return my_user_key.get()


def userLoggedIn():
    return True if currentUser() else False


def userExist():
    return True if userKey() else False


def newUser(user):
    MyUser(id=user.user_id()).put()


def usersAnagrams(my_user):
    if my_user:
        logging.debug(my_user.tweets)
        result = []

        for anagram in my_user.tweets:
            anagrams = anagram.get()
            result.append(anagrams)

        return result


def add_tweet(my_user, username, content, tags, tweet_key):
    if content:
        twitter = tweet_key.get()
        twitter.user_id = my_user.key.id()
        twitter.username = username
        twitter.content = content
        twitter.tags = tags
        twitter.put()
        my_user.tweets.append(tweet_key)
        my_user.put()


def add_newAnagram(my_user, username, content, tags, twitter_id, twitter_key):
    if text:
        twitter = Twitter(id=twitter_id)
        twitter.username = username
        twitter.content = content
        twitter.tags = tags
        twitter.put()
        my_user.tweets.append(twitter_key)
        my_user.put()


def add_newRegister(my_user, first_name, last_name, username, about, dob, userinfo_id, userinfo_key):
    if username:
        new_data = UserInfo(id=userinfo_id, username=username, first_name=first_name, last_name=last_name, about=about, dob=datetime.strptime(dob, '%Y-%m-%d'),user_id=my_user.key.id())
        new_data.put()
        my_user.tweets.append(userinfo_key)
        my_user.username = username
        my_user.put()
