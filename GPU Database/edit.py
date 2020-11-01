import os
import webapp2
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

from address import Address
from datetime import datetime
from myuser import MyUser

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class Edit(webapp2.RequestHandler):
    def get(self):

        url=''
        url_string=''
        welcome='Welcome back'

        # pull the user from the request

        user= users.get_current_user()

        if user:
            url = users.create_logout_url('/')
            url_string = 'logout'

        else:
            url=''
            users.create_login_url(self.request.uri)

        url_string='login'

        name = self.request.get('name')
        mygpu_key = ndb.Key('Address', name)
        my_gpu = mygpu_key.get()

        if my_gpu is None:
            self.redirect('/')
            return

        template_values = {
            'url': url,
            'url_string': url_string,
            'user': user,
            'welcome': welcome,
            'my_gpu': my_gpu,
            'checked': 'checked',
        }


        template = JINJA_ENVIRONMENT.get_template('edit.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        if self.request.get('button') == 'Update':

            name = self.request.get('my_gpu_name')
            dateissued = self.request.get('my_gpu_dateissued')
            manufacturer = self.request.get('my_gpu_manufacturer')

            if (self.request.get('my_gpu_geometryShader')):
                geometryShader = True
            else:
                geometryShader = False

            if (self.request.get('my_gpu_tesselationShader')):
                tesselationShader = True
            else:
                tesselationShader = False

            if (self.request.get('my_gpu_shaderInt16')):
                shaderInt16 = True
            else:
                shaderInt16 = False
            if (self.request.get('my_gpu_sparseBinding')):
                sparseBinding = True
            else:
                sparseBinding = False
            if (self.request.get('my_gpu_textureCompressionETC2')):
                textureCompressionETC2 = True
            else:
                textureCompressionETC2 = False
            if (self.request.get('my_gpu_vertexPipelineStoreandAtomics')):
                vertexPipelineStoreandAtomics = True
            else:
                vertexPipelineStoreandAtomics = False

            new_address = Address(id=name, name=name, manufacturer=manufacturer, dateissued=datetime.strptime(dateissued, '%Y-%m-%d'), geometryShader=geometryShader, tesselationShader=tesselationShader, shaderInt16=shaderInt16, sparseBinding=sparseBinding, textureCompressionETC2=textureCompressionETC2, vertexPipelineStoreandAtomics=vertexPipelineStoreandAtomics)

            new_address.put()
            self.redirect('/view')

        elif self.request.get('button') == 'Cancel':
            self.redirect('/')