import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mssg=b"hello" #convert to bytes we can also use mssg.encode()
s.sendto(msg,("192.168.43.99",1234))
