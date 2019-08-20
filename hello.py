from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h3>hello world</h3>")





if __name__ == '__main__':
    #创建web应用
    app = Application([
        ('/',IndexHandler)
    ])
    #绑定端口
    app.listen(7000)

    #启动web服务
    print('starting  http://localhost:%s'%7000)
    IOLoop.current().start()