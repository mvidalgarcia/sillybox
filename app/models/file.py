from google.appengine.ext import ndb


class File(ndb.Model):
    name = ndb.StringProperty()
    format = ndb.StringProperty()
    size = ndb.IntegerProperty()
    blob_key = ndb.BlobKeyProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
