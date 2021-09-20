import socket
#mention protocol(udp)
myp=socket.SOCK_DGRAM
#mention address family(ipv4)
afn=socket.AF_INET
s=socket.socket(afn,myp)

ip="192.168.43.66"
port=1234
s.bind((ip,port))

while True:
	x=s.recvfrom(1024) #1024 is maximum size of data it can recv
	clientip=x[1][0]
	msg=x[0].decode()
	print(clientip+":"+msg)
