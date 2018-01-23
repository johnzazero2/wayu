#!/usr/bin/env python

import socket


while True:
      data = int(raw_input("Enter number :"))
      TCP_IP = '127.0.0.1'
      TCP_PORT = 50019
      BUFFER_SIZE = 1024
      MESSAGE = data

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TCP_IP, TCP_PORT))
      s.send(str(MESSAGE))
      data = s.recv(BUFFER_SIZE)
      s.close()

      #Client received message from server 
      print "received data:", data
      
