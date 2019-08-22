from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler

from app.modles.menu import Menu
from utils.conn import session


class INdexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # data = {
        #     "msg":"hi,disen",
        #     "error_msg":"error",
        #     'age':20,
        #     'menus':['主页','新闻','音乐','视频'],
        #     'code':'<h3>hi,我是图片：8 > 5</h3>',
        #
        # }

        data = {
            "onetap":session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        }

        # self.set_header(name='X-Content-Type-Options',value='nosniff')
        self.render('user_curd.html',**data)
    def post(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass
