import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from sadness import SadnessFactory


 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")

    def post(self):
        zipcode = self.get_argument('zipcode')
        body = self.get_argument('body')
        number = self.get_argument('number')
        self.write(SF.process_text(number, body, zipcode))
 
def main():
    SF = SadnessFactory() 
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'static')}),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()

