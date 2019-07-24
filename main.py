import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        template = jinja_env.get_template('main.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())


        }
=======
        template = jinja_env.get_template('template/main.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
>>>>>>> e4e875446d5e3d12ede14dea6e3b6d0dc9f00d55


class MakePost(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        template = the_jinja_enviroment.get_template(" .html")
=======
        template = jinja_env.get_template("template/makePost.html")
>>>>>>> e4e875446d5e3d12ede14dea6e3b6d0dc9f00d55
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

    def post(self):
        # Use the user input to create a new blog post
        all_posts = Post.query().fetch()
        artist_input = self.request.get('artist')
        title_input = self.request.get('title')
        poem_input = self.request.get('poem')


        new_post = Post(artist= artist_input, title=title_input, poem=poem_input)
        new_post.put()
        # Add the new post to the beginning of our already-queried list of
         # posts
        all_posts.insert(0, new_post)

        # Render the template
        template_vars = {

             'all_posts': all_posts
         }
        template = the_jinja_env.get_template('templates/viewpage.html')
        self.response.write(template.render(template_vars))


class ViewPage(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        template = the_jinja_enviroment.get_template(" .html")
=======
        template = jinja_env.get_template("template/view.html")
>>>>>>> e4e875446d5e3d12ede14dea6e3b6d0dc9f00d55
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class AboutUs(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        template = the_jinja_enviroment.get_template(" .html")
=======
        template = jinja_env.get_template("template/aboutus.html")
>>>>>>> e4e875446d5e3d12ede14dea6e3b6d0dc9f00d55
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
