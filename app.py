# encoding=utf-8

import tornado.web
import tornado.ioloop
from tornado.web import url as url

import config
from view import main_view as mv


def build_app():
    return tornado.web.Application(handlers=[
        url(r'/url_popularize', mv.URL_Popularize),  # 网址推广
    ], **config.APP_SETTING)


if __name__ == "__main__":
    app = build_app()
    app.listen(config.PORT)
    tornado.ioloop.IOLoop.current().start()
