import json

from tornado.web import RequestHandler


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
