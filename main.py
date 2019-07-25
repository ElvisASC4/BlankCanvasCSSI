import jinja2
import os
import webapp2
from models import SavePost
from google.appengine.ext import ndb

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
        all_posts = SavePost.query().fetch()

        artist_input = self.request.get('artist')
        title_input = self.request.get('title')
        poem_input = self.request.get('poem')
        vote_num = self.request.get('vote_count')






        new_post = SavePost(artist= artist_input, title=title_input, poem=poem_input, vote_count=0)
        new_post.put()
        self.redirect('/View')

        upvote_var = (self.request.get("upvote"))

        if upvote_var == "upvote_value":
            vote_num = int(self.request.get('vote_count'))
            post_key=self.request.get("hidden")
            vote_num+=1

            new_post.vote_count=vote_num
            new_post.put()

         # posts
        # posts_by_new=
        all_posts.insert(0, new_post)
        # posts_ordered= posts_by_new.order(vote)

class ViewPost(webapp2.RequestHandler):
    def get(self):
        all_posts = SavePost.query().fetch()
        template_vars = {
                "all_posts":all_posts
                # "posts_ordered":posts_ordered
        }
        template = jinja_env.get_template("template/viewPost.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_vars))

    def post(self):
        all_posts = SavePost.query().fetch()
        post_key_url = self.request.get('postKey')
        post = ndb.Key(urlsafe = post_key_url).get()
        print post_key_url

        comment_input = self.request.get('comment')

        # print "hi there"

        print post
        post.comments.append(comment_input)
        post.put()

        # Render the template
        template_vars = {
                # "new_post":new_post,
                "all_posts":all_posts
                # "posts_ordered":posts_ordered
        }
        template = jinja_env.get_template(
            'template/viewPost.html')
        self.response.write(template.render(template_vars))
# class UpVote(webapp2.RequestHandler):
#     def post(self):
#         vote_num = self.request.get('vote_count')
#         vote_num+=1
#
#         new_post.vote_count=vote_num
#         new_post.put()
#
#         template_vars = {
#                 "new_post":new_post,
#                 # "posts_ordered":posts_ordered
#
#         }
#         template = jinja_env.get_template(
#             'template/viewPost.html')
#         self.response.write(template.render(template_vars))



class AboutUs(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("template/aboutus.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', WelcomePage),
    ('/View', ViewPost),
    ('/MakePost', MakePost),
    ('/AboutUs', AboutUs),

    ], debug=True)
