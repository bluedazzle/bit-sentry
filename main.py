# coding: utf-8
from __future__ import unicode_literals

import tornado.web
import os

from tasks import check_eth_eos, check_cls_news


class Application(tornado.web.Application):
    """
    tornado app 初始化
    """

    def __init__(self):
        handlers = [
            (r"/", IndexHandle),
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        super(Application, self).__init__(handlers, **settings)


class IndexHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello bit sentry')
        self.finish()


app = Application()
app.listen(8800)
tornado.ioloop.PeriodicCallback(check_cls_news, 1000 * 5).start()
tornado.ioloop.IOLoop.current().start()
