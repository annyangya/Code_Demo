import tornado
import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import options, define, parse_command_line
import os

import models
from urls import handlers

define("port", default=8080, help="port, default=8080")
define("debug", default=False, help="debug, default=False")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_url_prefix": "/static/",
    "template_path": os.path.join(os.path.dirname(__file__), "templates")
}


class Application(tornado.web.Application):
    def __init__(self):
        settings["debug"] = options.debug
        super().__init__(handlers, **settings)


if __name__ == '__main__':

    models.init_db()
    parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    if options.debug:
        print("run in debug mode")
    tornado.ioloop.IOLoop.instance().start()
