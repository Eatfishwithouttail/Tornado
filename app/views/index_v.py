from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler


class INdexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        wd = self.get_argument('wd')
        print(wd)
        wd1 = self.get_arguments('title')
        print(wd1)
        wd2 = self.get_query_argument('wd')
        print(wd2)
        title1 = self.get_query_arguments('title')
        print(title1)

        # request请求中的数据都属字典类型，字典中的value都是字节码
        req: HTTPServerRequest = self.request
        wd3 = req.arguments.get('wd')
        print(wd3)
        wd4 = req.query_arguments.get("wd")
        print(wd4)

        self.write('<h3>主页</h3>')

    def post(self, *args, **kwargs):
        # 新增数据
        resp = self.get_body_argument("city")
        resp1 = self.get_body_argument("name")
        print(resp1, resp)
        self.write("<h3>{{ %s }}</h3><h3>{{ %s }}</h3>" % (resp, resp1))

    def put(self, *args, **kwargs):
        self.write('<h3>PUT</h3>')

    def delete(self, *args, **kwargs):
        self.write('<h3>DELETE</h3>')
