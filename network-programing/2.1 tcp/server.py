#!/usr/bin/env python

import socket


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
while True:
    TCP_IP = '127.0.0.1'
    TCP_PORT = 50019
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        changtype = int(data)
        value = factorial(changtype)
        #print(value)
        conn.send(str(value))  # echo
    conn.close()
