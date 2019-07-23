


class ViewPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_enviroment.get_template(" .html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
        
class ViewPage(webapp2.RequestHandler):
    def get(self):





app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', WelcomePage),
    ('/View', View),
    ('/NewPost', NewPost),
    ('/friends', FriendsPage) #maps '/predict' to the FortuneHandler
], debug=True)
