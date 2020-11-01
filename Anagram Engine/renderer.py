import jinja2
import os
import utilities

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def render_login(self, url):
    template_values = {'url': url}

    template = JINJA_ENVIRONMENT.get_template('/templates/login.html')
    self.response.write(template.render(template_values))


def render_main(self, url, user, anagrams):
    template_values = {
        'url': url,
        'user': utilities.get_user(),
        'user1': user,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('/templates/main.html')
    self.response.write(template.render(template_values))


def render_addanagram(self, url, user, anagrams):
    template_values = {
        'url': url,
        'user': utilities.get_user(),
        'user1': user,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('/templates/addanagram.html')
    self.response.write(template.render(template_values))


def render_searchtext(self, url, value, input_text, anagrams):
    template_search_values = {
        'url': url,
        'user': utilities.get_user(),
        'value': value,
        'input_text': input_text,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('/templates/searchResult.html')
    self.response.write(template.render(template_search_values))


def render_upload(self, url, anagrams):
    template_search_values = {
        'url': url,
        'user': utilities.get_user(),
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('/templates/fileupload.html')
    self.response.write(template.render(template_search_values))


def render_subanagram(self, url, value, anagrams):
    template_search_values = {
        'url': url,
        'user': utilities.get_user(),
        'value': value,
        'anagrams': anagrams,
    }

    template = JINJA_ENVIRONMENT.get_template('/templates/subanagram.html')
    self.response.write(template.render(template_search_values))
