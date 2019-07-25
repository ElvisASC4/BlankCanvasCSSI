from google.appengine.ext import ndb


class SavePost(ndb.Model):
  artist = ndb.StringProperty()
  title = ndb.StringProperty()
  poem = ndb.TextProperty()
  vote_count = ndb.IntegerProperty()
  comments = ndb.TextProperty(repeated=True)
  code = ndb.StringProperty()




  # post = ndb.TextProperty()
