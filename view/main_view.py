# encoding=utf-8

import tornado.web
import config


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')


# 主页
class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


# 提供文件下载
class DownLoad_2345(BaseHandler):
    def get(self):
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', "attachment; filename=%s" % "p7_k58335833_djNm0u1xQ8Pm17BM8IqukPD.exe")
        buf_size = 2048

        with open(config.down_load_dir, 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                self.write(data)


# 处理URL导航
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
