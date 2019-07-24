from google.appengine.ext import ndb
import main

class SavePost(ndb.Model):
  artist = ndb.StringProperty()
  title = ndb.StringProperty()
  poem = ndb.StringProperty()

  new_post = SavePost(artist= artist_input, title=title_input, poem=poem_input)


  # post = ndb.TextProperty()
