from google.appengine.ext import ndb


class SavePost(ndb.Model):
  artist = ndb.StringProperty()
  title = ndb.StringProperty()
  poem = ndb.TextProperty()
  vote_count = ndb.IntegerProperty()
<<<<<<< HEAD
  code = ndb.StringProperty()
=======
  comment = ndb.TextProperty()
>>>>>>> f4701114038fce3fb07cc0205f0127f4da3efab6




  # post = ndb.TextProperty()
