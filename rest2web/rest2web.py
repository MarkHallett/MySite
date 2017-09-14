# rest2web.py

from tornado import websocket, web, ioloop
import json

cl = []

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("show_gbp_usd_eur.html")

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            print ('Append')
            cl.append(self)

    def on_close(self):
        if self in cl:
            print ('Remove')
            cl.remove(self)

class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        print ('!! get',args)
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        name = self.get_argument('name')
        data = {"id": id, "value" : value, "name":name}
        print ('!! get',data)
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)

    @web.asynchronous
    def post(self):
        print ('!! post')
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        name = self.get_argument('name')
        trade_time = self.get_argument('trade_time')
        data = {"id": id, "value" : value, "name":name, "trade_time": trade_time}
        print ('!! post',data)
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)

    @web.asynchronous
    def put(self,*args):
        print ('!! put',args)
        self.finish()
        id = 9 #self.get_argument("id")
        value = 123 #self.get_argument("value")
        name = 'usdeur' #self.get_argument('name')
        data = {"id": id, "value" : value, "name":name}
        print ('!! put',data)
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)


app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/api', ApiHandler),
    (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    (r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './'}),
])

if __name__ == '__main__':
    app.listen(8888)
    #app.listen(8888, address='0.0.0.0')
    ioloop.IOLoop.instance().start()
