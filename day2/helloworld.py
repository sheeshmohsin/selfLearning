import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class SecondHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world from second page")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/second", SecondHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
