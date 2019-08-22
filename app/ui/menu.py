from tornado.web import UIModule
from utils.conn import session
from app.modles.menu import Menu



class MenuMoudel(UIModule):
    def render(self):
        data = {
            'menus': session.query(Menu).filter(Menu.parent_id.is_(None)).all()
    }
        return self.render_string('ui/menu.html',**data)