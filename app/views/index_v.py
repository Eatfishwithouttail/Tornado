from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class INdexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        data = {
            "msg":"hi,disen",
            "error_msg":"error",
            'age':20,
            'menus':['主页','新闻','音乐','视频'],
            'code':'<h3>hi,我是图片：8 > 5</h3>',

        }
        self.render('index2.html',**data)
    def post(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass
