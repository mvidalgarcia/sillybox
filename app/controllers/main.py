import webapp2

from app.models.file import File
from google.appengine.ext.webapp.template import render
from google.appengine.ext import blobstore


class MainHandler(webapp2.RequestHandler):
    def get(self):
        """Handle GET requests."""
        upload_url = blobstore.create_upload_url('/upload_file')
        files = File.query()
        template = 'templates/index.html'
        context = {
            'files': files,
            'upload_url': upload_url
        }

        self.response.write(render(template, context))
