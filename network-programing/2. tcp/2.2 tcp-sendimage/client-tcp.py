import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
fileName = "image001.jpg"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "send picture:", fileName
fileOpen = open(fileName,'rb')
data = fileOpen.read(BUFFER_SIZE)
while (data):
    s.send(data)
    data = fileOpen.read(BUFFER_SIZE)
fileOpen.close()
print "sending complete"
s.close()

    

