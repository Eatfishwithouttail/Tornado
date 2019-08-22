from tornado.web import Application

from app.views.cookie_v import CookieHandler
from app.views.index_v import INdexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler


def make_app(host='localhost'):
    return Application([
        ('/', INdexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(\d+)/(\d+)',OrderHandler)
    ], default_host=host)