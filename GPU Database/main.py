import os
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

from myuser import MyUser
from address import Address
from datetime import datetime
from view import View
from edit import Edit
from myfeature import MyFeature
from compare import Compare

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        query = Address.query()
        data = query.fetch()

        if user == None:
            template_values = {
                'login_url' : users.create_login_url(self.request.uri),
                'addresses': data
            }

            template = JINJA_ENVIRONMENT.get_template('mainpage_guest.html')
            self.response.write(template.render(template_values))
            return

        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        if myuser == None:
            myuser = MyUser(id=user.user_id())
            myuser.put()

        template_values = {
            'logout_url': users.create_logout_url(self.request.uri),
            'addresses': data
        }
        template = JINJA_ENVIRONMENT.get_template('mainpage.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')

        if action == 'Add':

            gpu_key = ndb.Key('Address', self.request.get('name'))
            gpudata = gpu_key.get()
            Name = self.request.get('name')

            if gpudata != None:
                template_values = {
                    'Alreadyadded': ' GPU Already Exist',
                    'addresses': Address.query().fetch()
                }
                template = JINJA_ENVIRONMENT.get_template('mainpage.html')
                self.response.write(template.render(template_values))
            else:
                addresses = Address(id=self.request.get('name'))
                addresses.Key = self.request.get('name')


                name = self.request.get('name')
                manufacturer = self.request.get('manufacturer')
                dateissued = self.request.get('dateissued')
                if (self.request.get('geometryShader')):
                    geometryShader =True
                else:
                    geometryShader =False

                if (self.request.get('tesselationShader')):
                    tesselationShader =True
                else:
                    tesselationShader =False

                if (self.request.get('shaderInt16')):
                    shaderInt16 =True
                else:
                    shaderInt16 =False
                if (self.request.get('sparseBinding')):
                    sparseBinding =True
                else:
                    sparseBinding =False
                if (self.request.get('textureCompressionETC2')):
                    textureCompressionETC2 =True
                else:
                    textureCompressionETC2 =False
                if (self.request.get('vertexPipelineStoreandAtomics')):
                    vertexPipelineStoreandAtomics = True
                else:
                    vertexPipelineStoreandAtomics = False

                user = users.get_current_user()
                myuser_key = ndb.Key('MyUser', user.user_id())
                myuser = myuser_key.get()

                new_address = Address(id = name, name=name, manufacturer=manufacturer, dateissued=datetime.strptime(dateissued, '%Y-%m-%d'),
                                    geometryShader=geometryShader, tesselationShader = tesselationShader, shaderInt16 = shaderInt16,
                                    sparseBinding = sparseBinding, textureCompressionETC2 = textureCompressionETC2,
                                    vertexPipelineStoreandAtomics = vertexPipelineStoreandAtomics)
                myuser.addresses.append(new_address)
                new_address.put()

                self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/view', View),
    ('/edit', Edit),
    ('/myfeature', MyFeature),
    ('/compare', Compare),
])
