from google.appengine.ext import ndb


class SavePost(ndb.Model):
  artist = ndb.StringProperty()
  title = ndb.StringProperty()
  poem = ndb.TextProperty()
  vote_count = ndb.IntegerProperty()
  comment = ndb.TextProperty()




  # post = ndb.TextProperty()
