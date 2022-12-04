#!/usr/bin/python

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 8000))


server.listen(2)

#test_socket.accept() creates the client socket with ip and port number
(client, (ip, port)) = server.accept()

print "Conection received from client: ", ip

msg = "no message"

while len(msg):
    msg = client.recv(2048)
    print "Client: ", msg
    client.send(msg)

client.close()
server.close()

