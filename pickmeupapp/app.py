import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.auth
import tornadio2
import pymongo
import hashlib
import random
from datetime import datetime
from metatoe import *
import pickle

import smtplib
from email.MIMEText import MIMEText

from tornado.options import define, options
from tornado.escape import json_encode, json_decode
from tornado.web import HTTPError

define("address", default="", help="run on the given address", type=str)
define("port", default=8080, help="run on the given port", type=int)
define("debug", default=1, help="debug mode", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        conn = pymongo.Connection("localhost", 27017)
        self.db = conn['242fp']

        if options.debug == 0:
            options.debug = False
        else:
            options.debug = True

        # Will need login_url for settings
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            socket_io_port = options.port,
            socket_io_address = options.address,
        )
        print settings

        handlers = [
            (r"/", IndexHandler), 

            # favicon
            (r"/favicon.ico", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
   
        ]

        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    pass

class IndexHandler(BaseHandler):
    def get(self):
        u = self.get_current_user()
        self.render("index.html", user=u.get('handle', None))



#Set up webserver and create admin account 'KAM'
def main():
    tornado.options.parse_command_line()
    application = Application()

    tornadio2.server.SocketServer(application)

if __name__ == "__main__":
    main()

