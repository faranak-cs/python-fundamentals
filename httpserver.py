#!/usr/bin/env python3

import http.server
import socketserver

PORT = 8000

class httpRequestHandler(http.server.SimpleHTTPRequestHandler) :
    def do_GET(self):
        if self.path == '/admin':
            self.wfile.write("This is only for ADMINS")
            self.wfile.write(self.headers)

        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)

httpserver = socketserver.TCPServer(('', PORT), httpRequestHandler)

print("Server started at port ", PORT)
httpserver.serve_forever()
