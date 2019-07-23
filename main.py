import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('template/main.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())


class MakePost(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("template/makePost.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

    def post(self):
        # Use the user input to create a new blog post
        artist_input = self.request.get('artist')
        title_input = self.request.get('title')
        poem_input = self.request.get('poem')


        new_post = Post(artist= artist_input, title=title_input, poem=poem_input)
        new_post.put()


class ViewPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("template/view.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class AboutUs(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("template/aboutus.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', WelcomePage),
    ('/View', ViewPage),
    ('/MakePost', MakePost),
    ('/AboutUs', AboutUs) #maps '/predict' to the FortuneHandler
], debug=True)
