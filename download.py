import socket 
import time
import tqdm
import os
import glob

s=socket.socket()

s.bind(('127.0.0.1', 12335))

s = socket.socket()   
s.bind(('127.0.0.1', 12335))     
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
print (s.recv(1024).decode())
service="download"

cred="yash yash123 192.168.22.3 "+service

 
print("Message initialized")

s.send(cred.encode())
 
print("Message sent")
##########################################################

Allports = s.recv(1024).decode()
 
print(Allports)
print("Message receved")

# close the connectionq
s.close()    
print("Socket Closed")
credF="Yash yash123 IP_address"
time.sleep(5)
 
 
ports=Allports.split()
i=0

if(service=="download"):
	BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

	for i in range(len(ports)):
		s1-socket.socket()
		port1=12345
		s1.bind(("127.0.0.1",port1))
		
		if(decCred[3]=="download"):
            
        	BUFFER_SIZE = 4096
        	SEPARATOR = "<SEPARATOR>"
        	rec=c1.recv(1024).decode()
        	print(rec)
        	c1.send("hi".encode())
        	received = c1.recv(BUFFER_SIZE).decode()
        	global filename
        	global filesize
        	filename, filesize = received.split(SEPARATOR)
        	filename = os.path.basename(filename)
        	filesize = int(filesize)
        	progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        	with open(filename, "wb") as f:
          	while True:
    
         
            	bytes_read = c1.recv(BUFFER_SIZE)
            	if not bytes_read:    
            
                	break
       
            	f.write(bytes_read)
        
            	progress.update(len(bytes_read))


   
        	c1.close()
        	s1.close()
