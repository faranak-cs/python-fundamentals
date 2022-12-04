#!/usr/bin/python

import SimpleHTTPServer, SocketServer


class httpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler) :
    def do_GET(self):
        if self.path == '/admin':
            self.wfile.write("This is only for ADMINS")
            self.wfile.write(self.headers)

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpserver = SocketServer.TCPServer(('', 10001), httpRequestHandler)

httpserver.serve_forever()



