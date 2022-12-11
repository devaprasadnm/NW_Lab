import socket
import math

host = "127.0.0.1"
port = 12345
key = "hack"

def trans_encrypt(msg,key):
	li = list(msg)
	li_k = list(key)
	li_ks = list(key)
	li_ks.sort()
	
	cipher = ""
	
	l_key,l_pt = len(key),len(msg)
	col = l_key
	row = int(math.ceil(l_pt/col))
	
	no_null = (row*col)-l_pt
	
	li.extend("_"*no_null)
	
	
	matrix  = []
	
	for i in range(0,len(li),col):
		matrix.append(li[i:i+col])
		
	ans = []
	
	for i in li_ks:
		x = li_k.index(i)
		for j in range(row):
			ans.append(matrix[j][x])
			
			
	return cipher.join(ans)
		
	
	
	

with socket.socket() as s:
	s.connect((host,port))
	msg = input("Enter the message : ")
	cipher = trans_encrypt(msg,key)
	s.send(cipher.encode())
	s.close()
	
