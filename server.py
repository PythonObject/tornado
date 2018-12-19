# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     server.py
   Description :   tornado server
   Author :        wu ming ming
   date：
-------------------------------------------------
   Change Activity:
                2018/12/19 : create file
-------------------------------------------------
"""
__author__ = 'wumingming'

from tornado import web
from tornado import ioloop

class MainHandler(web.RequestHandler):
    """"""

    def get(self):
        self.write("hello tornado")

if __name__ == "__main__":

    app = web.Application(handlers=[(r"/", MainHandler),], default_host="localhost")
    app.listen(port=8090)
    ioloop.IOLoop.current().start()
    pass
