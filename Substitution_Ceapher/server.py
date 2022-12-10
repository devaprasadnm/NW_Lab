import socket
import string

host = "127.0.0.1"
port = 12345

key = 3
list1 = list(string.ascii_lowercase)


def decryption(data,key):
	plane_text = ""
	for i in data:
		c = list1.index(i)
		plane_text += list1[(c-key)%26]
	return plane_text

with socket.socket() as s:
	s.bind((host,port))
	print("socket connected successfully")
	s.listen()
	print("listening....")
	conn,addr = s.accept()
	
	while True:
		msg = conn.recv(1024).decode()
		print(f"Message :{msg}")
		data = decryption(msg,key)
		print(f"Encrypted message :{data}")
		conn.close()
		break
