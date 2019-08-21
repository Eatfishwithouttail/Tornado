import json

from tornado import options
from tornado.httputil import HTTPServerRequest
from tornado.ioloop import IOLoop
from tornado.options import define
from tornado.web import Application
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


class SearchHandler(RequestHandler):
    mapper = {
        'python': 'python是目前世界最流行的AI语言',
        'java': 'java已经是20多年企业应用开发语言',
        'H5': 'H5全称是Html5，于2014年流行的标签语言'
    }

    def get(self):
        html = '''
            <h3>搜索%s结果</h3>
            <p>%s</p>
        '''

        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)
        # self.write(html%(wd,result))
        resp_data = {
            'wd': wd,
            'result': result
        }
        self.write(json.dumps(resp_data))
        self.set_status(200)
        self.set_header('Content-Type', 'application/json:charset=utf-8')

        self.set_cookie('wd', wd)


class CookieHandler(RequestHandler):
    def get(self):
        # 验证参数中是否存在name？
        if self.request.arguments.get('name'):
            name = self.get_query_argument('name')
            value = self.get_cookie(name)
            self.write(value)
        else:
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            lis = []
            for key in cookies:
                lis.append('<li>%s:%s</li>' % (key, self.get_cookie(key)))

            html2 = '''
                            <form method='post' onclick=delete()>
                                <input name='name'>
                                <button type='submit'>提交</button>
                            </form>
                        '''
            self.write('显示所有cookie' + html % ''.join(lis)+html2)

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            self.clear_cookie(name)
            self.write('删除%s成功' % name)
        else:
            self.write('删除%s失败，不存在' % name)
        #重定向操作时，不需要再调用self.write()
        self.redirect('/cookie')




class OrderHandler(RequestHandler):
    goods = [
        {
            'id':1,
            'name':'python高级开发',
            'author':'disen',
            'price':190
        },
        {
            'id': 2,
            'name': 'python高级开发',
            'author': 'disen',
            'price': 290
        }
    ]


    action_map = {
        1:'取消订单',
        2:'再次购买',
        3:'评价',
    }


    def query(self,order_id):
        for good in self.goods:
            if good.get('id') == order_id:
                return good

    def get(self,order_id,action_code):
        print("")

        self.write("订单查询")
        html = '''
            <p>商品编号：%s</P>
            <p>商品名称：%s</P>
            <p>商品作者：%s</P>
            <p>商品价格：%s</P>
            <p>动作：%s</P>
        '''
        good = self.query(int(order_id))
        action = self.action_map.get(int(action_code))
        self.write(html%(good.get('id'),good.get('name'),good.get('author'),good.get('price'),action))
        # self.write(self.action_map.get(int(action_code)))

    def initialize(self):
        print("----initialize----")

    def prepare(self):
        print('-----prepare-----')

    def on_finish(self):
        print("------finish-----")

def make_app():
    return Application([
        ('/', INdexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(\d+)/(\d+)',OrderHandler)
    ], default_host=options.options.host)


if __name__ == '__main__':
    define('port', default=8000, type=int, help="you server port ")
    define('host', default='0.0.0.0', type=str, help='host name')
    options.parse_command_line()

    app = make_app()
    app.listen(options.options.port)

    print("starting web server http://%s:%s" % (options.options.host, options.options.port))
    IOLoop.current().start()
