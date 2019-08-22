
from tornado.web import RequestHandler





class UserHandler(RequestHandler):
    def get(self):








        self.render_string('/user/user.html')
