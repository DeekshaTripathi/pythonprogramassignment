#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.43.142",7777))
#for i in range(1000) :
n1=s.recvfrom(1000)
n2=s.recvfrom(1000)

	
#print s.recvfrom(1000)
print (n1[0])
print (n2[0])
       # s.sendto("hii",("192.168.43.142",7777)) 
