from google.appengine.ext import ndb

class PostPost(ndb.Model):
  artist = ndb.StringProperty()
  poem = ndb.StringProperty()
  # post = ndb.TextProperty()
  
