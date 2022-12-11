import socket
from _thread import *

host = ""
port = 12345
clients = []

def sendToAll(msg,conn):
	for c in clients:
		if(c!=conn):
			c.send(msg.encode())

def handleClients(conn,addr):
	name = conn.recv(1024).decode()
	print(f"{name} connected to the server")
	while True:
		msg = conn.recv(1024).decode()
		if msg:
			sendToAll(name+':'+msg,conn)
			print(name+':'+msg)
		

with socket.socket() as s:
	s.bind((host,port))
	print("Socket connected")
	s.listen()
	print("Socket is listening...")
	
	while True:
		conn,addr = s.accept()
		clients.append(conn)
		start_new_thread(handleClients,(conn,addr))
		
