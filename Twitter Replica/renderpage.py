import jinja2
import os
import utilities

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def login(self, url):
    template_values = {'url': url}

    template = JINJA_ENVIRONMENT.get_template('loginpage.html')
    self.response.write(template.render(template_values))


def main(self, url, my_user, user, data, tweets):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'user': user,
        'data': data,
        'tweets': tweets,
    }

    template = JINJA_ENVIRONMENT.get_template('mainpage.html')
    self.response.write(template.render(template_values))

def register(self, url, my_user):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
    }

    template = JINJA_ENVIRONMENT.get_template('registerpage.html')
    self.response.write(template.render(template_values))


def edit(self, url, my_user, data):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'data': data,
    }

    template = JINJA_ENVIRONMENT.get_template('edituserinfo.html')
    self.response.write(template.render(template_values))


def add(self, url, my_user, data, url1):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'tweets': data,
        'url1': url1,
    }

    template = JINJA_ENVIRONMENT.get_template('addnewtweet.html')
    self.response.write(template.render(template_values))


def edittweet(self, url, my_user, data, value):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'data': data,
        'value': value,
    }

    template = JINJA_ENVIRONMENT.get_template('editthetweets.html')
    self.response.write(template.render(template_values))


def searchtext(self, url, my_user, data, data1, value):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'tweets': data,
        'userinfo': data1,
        'value': value,
    }

    template = JINJA_ENVIRONMENT.get_template('searchtweets.html')
    self.response.write(template.render(template_values))

def user(self, url, my_user, data, data1, value):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'tweets': data,
        'userinfo': data1,
        'value': value,
    }

    template = JINJA_ENVIRONMENT.get_template('searchusers.html')
    self.response.write(template.render(template_values))

def profile(self, url, my_user, tweets, userinfo):
    template_values = {
        'url': url,
        'user': utilities.currentUser(),
        'my_user': my_user,
        'tweets': tweets,
        'userinfo': userinfo,
    }

    template = JINJA_ENVIRONMENT.get_template('profilepage.html')
    self.response.write(template.render(template_values))
