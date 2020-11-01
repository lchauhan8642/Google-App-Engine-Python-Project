import os
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

from address import Address
from myuser import MyUser

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MyFeature(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()

        if self.request.get('my_gpu_geometryShader'):
            geometryShader = True
        else:
            geometryShader = False

        if self.request.get('my_gpu_tesselationShader'):
            tesselationShader = True
        else:
            tesselationShader = False

        if self.request.get('my_gpu_shaderInt16'):
            shaderInt16 = True
        else:
            shaderInt16 = False

        if self.request.get('my_gpu_sparseBinding'):
            sparseBinding = True
        else:
            sparseBinding = False

        if self.request.get('my_gpu_textureCompressionETC2'):
            textureCompressionETC2 = True
        else:
            textureCompressionETC2 = False

        if self.request.get('my_gpu_vertexPipelineStoreandAtomics'):
            vertexPipelineStoreandAtomics = True
        else:
            vertexPipelineStoreandAtomics = False

        query = Address.query(Address.geometryShader == geometryShader, Address.tesselationShader == tesselationShader, Address.shaderInt16 == shaderInt16, Address.sparseBinding == sparseBinding, Address.textureCompressionETC2 == textureCompressionETC2, Address.vertexPipelineStoreandAtomics == vertexPipelineStoreandAtomics)
        data = query.fetch()

        if user == None:
            template_values = {
                'login_url': users.create_login_url(self.request.uri),
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
        template = JINJA_ENVIRONMENT.get_template('myfeature.html')
        self.response.write(template.render(template_values))

        if self.request.get('button') == 'Cancel':
            self.redirect('/')
