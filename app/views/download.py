from tornado.httpclient import HTTPClient, HTTPResponse,HTTPRequest
from tornado.web import RequestHandler


class DownLoadHandle(RequestHandler):
    def get(self):
        #获取参数的url（下载资源的路径）
        url = self.get_query_argument("url")
        filename = self.get_query_argument('filename','index.html')
        #发起同步请求
        client = HTTPClient()
        resp: HTTPResponse  = client.fetch(url,validate_cert=False)
        # print(resp.body)
        #保存到static目录下static/downloads
        from app import BASE_DIR,os
        dir = os.path.join(BASE_DIR,"static/downloads")

        with open(os.path.join(dir,filename),"wb") as f:
            f.write(resp.body)


        self.write("下载成功！！")