import webapp2

from app.models.file import File
from google.appengine.ext.webapp.template import render


class MainHandler(webapp2.RequestHandler):
    def get(self):
        """Handle GET requests."""

        files = File.query()
        template = 'templates/index.html'
        context = {
            'files': files,
        }

        self.response.write(render(template, context))
