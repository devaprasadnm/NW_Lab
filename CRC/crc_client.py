import socket

host="127.0.0.1"
port=1234

key = "1101"

def xor(a,b):
	res=""
	for i in range(1,len(a)):
		if a[i] == b[i]:
			res=res+'0'
		else:
			res=res+'1'
	return res


def bin_division(data,key):
	pick = len(key)
	len_data = len(data)
	
	tmp = data[0:pick]
	
	while(pick<len_data):
		if tmp[0] == '1':
			tmp = xor(tmp,key) + data[pick]
		else:
			tmp = xor(tmp,'0'*len(key)) + data[pick]
			
		pick+=1
		
	if tmp[0] == '1':
		tmp = xor(tmp,key) 
	else:
		tmp = xor(tmp,'0'*len(key))
		
	return tmp

def crc(data,key):
	l=len(key)-1
	enc_data = data+"0"*l
	r = bin_division(enc_data,key)
	t_data = data+r
	return t_data
	
	
with socket.socket() as s:
	s.connect((host,port))
	print("socket created")
	
	msg = input("Enter the message : ")
	
	trans_data = crc(msg,key)
	print(f"Transmitted Message : {trans_data}")
	
	s.send(trans_data.encode())
	s.close()
