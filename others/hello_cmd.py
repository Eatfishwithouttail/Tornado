import tornado.web as web
import  tornado.ioloop as ioloop
from tornado.options import define,options,parse_command_line


define("port",default=8000,type=int,help='set you server port')

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("hello,dsien")


class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        world = self.get_argument("wd")
        self.write("hello za")


class LogoutHander(web.RequestHandler):
    def get(self, *args, **kwargs):
        word = self.get_argument('wd')
        self.set_status(status_code=300)
        self.write("hello, %s"% word)


if __name__ == '__main__':
    #解析命令行的参数
    parse_command_line()
    app = web.Application([
        ('/',IndexHandler),
        ('/login',LoginHandler),
        ('/logout',LogoutHander)
    ])

    app.listen(options.port)

    ioloop.IOLoop.current().start()