import socket

while True:
      data = int(input("Enter number :"))
      UDP_IP = "127.0.0.1"
      UDP_PORT = 50015
      MESSAGE = data

      print "UDP target IP:", UDP_IP
      print "UDP target port:", UDP_PORT
      
      #Client send message to server 
      print "\nClient send message to server :", MESSAGE
      sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
      sock.sendto(str(MESSAGE), (UDP_IP, UDP_PORT)) #str

      #Server response to Clinet
      data, addr = sock.recvfrom(1024)
      #print "message:", MESSAGE
      print '\nServer response : ' + data
         
