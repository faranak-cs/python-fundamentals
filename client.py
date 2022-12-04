#!/usr/bin/python


import sys, socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((sys.argv[1], 8000))


while 1:
    msg = raw_input("Enter your message: ")
    client.send(msg)
    print client.recv(2048)


client.close()

