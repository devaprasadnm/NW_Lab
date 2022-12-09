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
	r = bin_division(data,key)
	return r
	

with socket.socket() as s:
	s.bind((host,port))
	print("socket created")
	s.listen()
	print("socket listening......")
	
	conn,arr = s.accept()
	
	while True:
		msg = conn.recv(1024).decode()
		
		print(f"Recieving Data: {msg}")
		
		rem = crc(msg,key)
		
		print(f"Remainder: {rem}")
		
		if rem == "000":
			print(f"Data containing No Error \nData :{msg[0:(len(msg)-len(key)+1)]}")
		else:
			printf("Data containing errors")
		
		conn.close()
		break
	
