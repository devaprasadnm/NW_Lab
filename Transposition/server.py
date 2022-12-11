#Columnar Transpositon
import socket
import math

host = "127.0.0.1"
port = 12345
key = "hack"

def trans_decrypt(msg,key):
	li = list(msg)
	li_k = list(key)
	li_ks = list(key)
	li_ks.sort()
	
	pt = ""
	
	l_key,l_pt = len(key),len(msg)
	row = l_key
	col = int(math.ceil(l_pt/row))
	
	#no_null = (row*col)-l_pt	
	#li.extend("_"*no_null)
	
	
	matrix  = []
	
	for i in range(0,len(li),col):
		matrix.append(li[i:i+col])
		
	
		
	ans = []
	
	for j in range(col):
		for i in li_k:
			x=li_ks.index(i)
			ans.append(matrix[x][j])
			
	pt = pt.join(ans)
	
	pt = pt.replace("_","")
	return pt
		

with socket.socket() as s:
	s.bind((host,port))
	print("Soicket connected")
	s.listen()
	print("listening ....")
	conn , addr = s.accept()
	
	while True:
		msg = conn.recv(1024).decode()
		print(f"Message recieved:  {msg}")
		pt = trans_decrypt(msg,key)
		print(f"Original message : {pt}")
		conn.close()
		break
