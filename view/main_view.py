# encoding=utf-8

import tornado.web
import config


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("网站正在部署中")


class URL_Popularize(BaseHandler):
    def get(self, *args, **kwargs):
        user_ip = self.request.remote_ip
        ready_url = config.url_popularize[0]

        try:
            user_access_val = config.url_ip_list[user_ip]
            if user_access_val >= len(config.url_popularize):
                ready_url = config.url_popularize[0]
            else:
                ready_url = config.url_popularize[user_access_val]
                config.url_ip_list[user_ip] = user_access_val + 1
        except KeyError:
            ready_url = config.url_popularize[0]
            config.url_ip_list[user_ip] = 1

        self.redirect(ready_url)
