import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line

define("port", default=8080, help="run on the given port", type=int)

# we gonna store clients in dictionary..
clients = dict()

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")
        # self.write("This is your response")
        # self.finish()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        self.id = kwargs["Id"]
        # self.stream.set_nodelay(True)
        print self.id, self
        clients[self.id] = {"id": self.id, "object": self}

    def on_message(self, message):        
        """
        when we receive some message we want some message handler..
        for this example i will just print message to console
        """
        print "Client %s received a message : %s" % (self.id, message)
        self.write_message("Conn!")
        
    def on_close(self):
        if self.id in clients:
            del clients[self.id]

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/(?P<Id>\w*)', WebSocketHandler),
])

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
