import webapp2

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from app.models.file import File


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            upload = self.get_uploads()[0]
            upload_file = File(
                name=upload.filename,
                format=upload.content_type,
                size=upload.size,
                blob_key=upload.key())
            upload_file.put()

            self.redirect('/')

        except:
            self.error(500)


class ViewHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, file_key):
        if not blobstore.get(file_key):
            self.error(404)
        else:
            self.send_blob(file_key)
