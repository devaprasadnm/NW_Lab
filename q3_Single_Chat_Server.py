# single chat 

# Server prgrm

import socket

print("Welcome to chatroom")
name =  input("Enter your name : ")
host = 'localhost'
port = 1234

with socket.socket() as s:
	print("socket created")

	s.bind((host,port))

	s.listen()
	print("\n Waiting for connections ... ")
	conn,addr = s.accept()

	s_name =  conn.recv(1024).decode()
	print(f"{s_name} has connected to this chatroom")
	print("Warning : To exit press 0")
	conn.send(name.encode())

	while True:
		msg = input("Me : ")
		if msg == '0':
			msg = "left chat room"
			conn.send(msg.encode())

			break
		conn.send(msg.encode())
		msg = conn.recv(1024).decode()
		print(f"{s_name} : {msg}")
