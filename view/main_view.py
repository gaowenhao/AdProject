# encoding=utf-8

import tornado.web
import random
import config


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')


class URL_Popularize(BaseHandler):
    def get(self, *args, **kwargs):
        ready_url = random.choice(config.url_popularize)
        self.redirect(ready_url);
