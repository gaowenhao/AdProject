# encoding=utf-8
import threading

import tornado.web
import tornado.ioloop
from tornado.web import url as url

import config
import tools
from view import main_view as mv


def build_app():
    return tornado.web.Application(handlers=[
        url(r'/url_popularize', mv.URL_Popularize),  # 网址推广
    ], **config.APP_SETTING)


if __name__ == "__main__":
    # 开启每日清理任务
    threading.Thread(target=tools.task_start_day_hour, args=[tools.clear_config_ip_days]).start()

    app = build_app()
    app.listen(config.PORT)
    tornado.ioloop.IOLoop.current().start()
