
 
import socket   
import os 
import time
import tqdm
 

 
 
s = socket.socket()        
print ("Socket successfully created")
 
 
 
port = 12346               
 

s.bind(('127.0.0.1', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
#while True:
 
# Establish connection with client.
c, addr = s.accept()    
print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type.
   

 
 
# Instance the Fernet class with the key
 
 
portrep=c.recv(1024).decode()
c.send("recevd".encode())
decCred=c.recv(1024).decode()
c.send("receved".encode())
 
print(decCred)
decCred=decCred.split()
 
c.close()

 
  # Close the connection with the client
s1=socket.socket()
port1 = 60001
s1.bind(('127.0.0.1', port1))
s1.listen(5)
 
c1, addr1 = s1.accept()

if(decCred[3]=="upload"):
  
   
  BUFFER_SIZE = 4096
  SEPARATOR = "<SEPARATOR>"

  rec=c1.recv(1024).decode()
  print(rec)
  c1.send("hi".encode())
  received = c1.recv(BUFFER_SIZE).decode()
  filename, filesize = received.split(SEPARATOR)
  print(filesize)
  filename = os.path.basename(filename)
  filesize = int(filesize)
  print(filesize)
  progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
  with open(filename, "wb") as f:
    while True:
    
         
      bytes_read = c1.recv(BUFFER_SIZE)
      if not bytes_read:    
            
          break
       
      f.write(bytes_read)
        
      progress.update(len((bytes_read)))

   
  c1.close()
  s1.close()
elif(decCred[3]=="download"):
  BUFFER_SIZE = 4096
  SEPARATOR = "<SEPARATOR>"

   
  filename=files[i] 
  filename=str(filename)
  print(filename)
  filesize = os.path.getsize(filename) 
  s1 = socket.socket() 
      
  print("server "+str(i)+" on")
  s1.connect(('127.0.0.1',int(ports[i])))

  s1.send("hloo".encode())
  rec=s1.recv(1024).decode()
  print(rec)
     
  s1.send(f"{filename}{SEPARATOR}{filesize}".encode())
  progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
  with open(filename, "rb") as f:
    while True:
         
      bytes_read = f.read(BUFFER_SIZE)
      if not bytes_read:
             
          break
         
      s1.sendall(bytes_read)
          
      progress.update(len(bytes_read))
   
   

         
  s1.close()
  i=i+1
        
  time.sleep(2)

 
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
portrep=portrep.split()
i=0
for i in range(len(portrep)):
  filename=str(filename)
   
  filesize = int(filesize)
  s=socket.socket()
  print(portrep[i])
  s.connect(('127.0.0.1',int(portrep[i])))
  s.send("hloo".encode())
  rec=s.recv(1024).decode()
  s.send(f"{filename}{SEPARATOR}{filesize}".encode())
  progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
  with open(filename, "rb") as f:
    while True:
      bytes_read = f.read(BUFFER_SIZE)
      if not bytes_read:
        break

      s.sendall(bytes_read)
      progress.update(len(bytes_read))

  s.close()
  i=i+1
  time.sleep(2)

   