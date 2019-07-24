from google.appengine.ext import ndb
import main

class SavePost(ndb.Model):
  artist = ndb.StringProperty()
  title = ndb.StringProperty()
  poem = ndb.StringProperty()

  

  # post = ndb.TextProperty()
