from google.appengine.ext import ndb


class SavePost(ndb.Model):
  artist = ndb.StringProperty()
  title = ndb.StringProperty()
  poem = ndb.TextProperty()




  # post = ndb.TextProperty()
