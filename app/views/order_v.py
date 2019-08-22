from tornado.web import RequestHandler


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