import os

from tornado.web import Application

from app.ui.menu import MenuMoudel
from app.views.cookie_v import CookieHandler
from app.views.index_v import INdexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler
from app.views.user import UserHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)


settings = {
    'debug':True,
    'template_path':os.path.join(BASE_DIR,'templates'),
    'static_path':os.path.join(BASE_DIR,'static'),
    'static_url_prefix':'/s/',
    'ui_modules':{
        'Menu':MenuMoudel
    }
}


def make_app(host='localhost'):
    return Application(
        handlers=[('/', INdexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(\d+)/(\d+)',OrderHandler),
        ('/user',UserHandler)],
        default_host=host,**settings)