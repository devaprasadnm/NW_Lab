import socket
from _thread import *
import select
import sys

host = "127.0.0.1"
port = 12345

with socket.socket() as s:
	s.connect((host,port))
	print("socket connected")
	name = input("Enter the name: ")
	s.send(name.encode())
	while True:
		socketList  = [sys.stdin,s]
		rList,wList,errList = select.select(socketList,[],[])
		for i in rList:
			if i == s:
				msg = i.recv(1024).decode()
				if msg :
					print(msg)
			else:
				msg = sys.stdin.readline()
				s.send(msg.encode())
				sys.stdout.write("You:")
				sys.stdout.write(msg)
				sys.stdout.flush()
		
