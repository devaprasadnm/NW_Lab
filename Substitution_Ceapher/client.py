import socket
import string

host = "127.0.0.1"
port = 12345

key = 3
list1 = list(string.ascii_lowercase)

def encryption(data,key):
	data.lower()
	cipher = ""
	for i in data:
		p = list1.index(i)
		cipher += list1[(p+key)%26]
	return cipher	

with socket.socket() as s:
	s.connect((host,port))
	print("socket connected..")
	data = input("Enter the input :")
	
	cipher = encryption(data,key)
	
	
	s.send(cipher.encode())
	s.close()
	
