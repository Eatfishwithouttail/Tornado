from tornado.web import RequestHandler


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