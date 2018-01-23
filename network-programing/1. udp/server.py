import socket

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

UDP_IP = "127.0.0.1"
UDP_PORT = 50015

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    
    #server calculate data
    changtype = int(data)
    value = factorial(changtype)
    
    #print(value)
    sock.sendto(str(value),addr)
    
    

    

