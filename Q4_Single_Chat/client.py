# Single chat
# client prgrm
import socket

host = 'localhost'
port = 1234

with socket.socket() as s:

	s.connect((host,port))

	print("WElcome to chatroom")
	name=input("Enter your name: ")

	s.send(name.encode())

	s_name=s.recv(1024).decode()


	print(f"{s_name} has joined chat room,Enter 0 to exit")


	while True:

		msg=s.recv(1024).decode()
		print(f"{s_name} :{msg}")

		msg=input("Me:")
		if msg == '0':

			msg="chat closed"
			s.send(msg.encode())
			break

		s.send(msg.encode())
