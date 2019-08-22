import json
import uuid

from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define,parse_command_line,options




class LoginHandler(RequestHandler):

    users = [{
        "id":1,
        'name':'disen',
        'pwd':'123',
        'last_login_device':'Android 5.1 OnePlus5'
    }]
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type，x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE')
        self.set_header('Content-Type', 'application/json')


    def options(self):
        self.set_status(200)

    def get(self):
        #读取json数据
        bytes = self.request.body
        print(bytes)
        print(self.request.headers.get('Content-Type'))
        content = self.request.headers.get('Content-Type')

        if content.startswith('application/json'):
            # self.write('uoload json ok')
            json_str = bytes.decode("utf-8")
            json_data = json.loads(json_str)

            resp_data = {}
            login_user = ''
            for user in self.users:
                if user['name'] ==  json_data['name']:
                    if user['pwd'] == json_data['pwd']:
                        login_user = user
                        break
            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '查无此用户'
            self.set_header('Content-Type','application/json')
            self.write(resp_data)


            # self.write(json_data['name'])
            # self.write(json_data['pwd'])

        else:
            self.write('upload data must json')
        # html = '''
        #     <form>
        #         用户登录：<input type='text' name='name'><br>
        #         用户口令：<input type='passwd' name='passwd'><br>
        #         <button>登录</button>&nbsp;<a href='#'>没有账号，点此注册</a>
        #     </form>
        # '''
        self.write('login')
        # self.cors()
    def post(self):
        bytes = self.request.body
        # print(bytes)
        content = self.request.headers.get('Content-Type')
        # print(content)


        if content.startswith('application/json'):
            #获取传来数据，并将其反序列化
            json_str = bytes.decode('utf-8')
            json_data = json.loads(json_str)
            # print(json_data)
            #判断是否拥有"mobile_type"属性，没有设置默认值
            json_data.setdefault("mobile_type",'pc')
            #设置用户id
            json_data['id'] = self.users[-1]['id'] + 1
            print(json_data)
            #增加到用户组中
            self.users.append(json_data)
            print(self.users)
            #返回新增用户id
            resp = {}
            resp['new_user_id'] = self.users[-1]['id']
            resp['token'] = uuid.uuid4().hex
            self.write(resp)


    def put(self):
        json_data = self.query_upload()
        print(json_data)
        # 查看需要修改的属性
        id = json_data['user_id'] -1
        user = self.users[id]
        resp = {}
        for keys,values in json_data.items():
            user[keys] = values

        resp['msg'] = 'success'

        self.write(resp)




    def delete(self):
        data = self.query_upload()
        id = data['user_id'] -1
        self.users.remove(self.users[id])
        resp = {}
        resp['msg'] = 'sucess'
        self.write(resp)


    def query_upload(self):
        json_str = self.request.body
        json_str = json_str.decode('utf-8')
        json_data = json.loads(json_str)
        return json_data



def make_app():
    return Application([
        ('/',LoginHandler)
    ],default_host=options.host)

if __name__ == '__main__':

    define("port",default=8000,type=int,help='port')
    define('host',default='localhost',type=str,help='主机ip')

    parse_command_line()  #解析命令行参数
    print("http://%s:%s"%(options.host,options.port))
    app = make_app()

    app.listen(options.port)
    IOLoop.current().start()