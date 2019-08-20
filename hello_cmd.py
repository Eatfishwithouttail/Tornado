import tornado.web as web
import  tornado.ioloop as ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("hello,dsien")


class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello za")


class LogoutHander(web.RequestHandler):
    def get(self, *args, **kwargs):

        self.write("hello, mrx")


if __name__ == '__main__':
    app = web.Application([
        ('/',IndexHandler),
        ('/login',LoginHandler),
        ('/logout',LogoutHander)
    ])

    app.listen(8000)

    print('starting  http://localhost:%s' % 8000)
    ioloop.IOLoop.current().start()