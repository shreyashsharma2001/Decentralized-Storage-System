from flask import Flask, render_template, Response, request, redirect, url_for

import socket 
import time
import tqdm
import os
import glob


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/forward/", methods=["POST"])
def move_forward():
    s = socket.socket()   
    s.bind(('127.0.0.1', 12335)) 
    forward_message = "Moving Forward..."
    return render_template("upload.html", forward_message=forward_message)
 

         
 
# Create a socket object
s = socket.socket()   
s.bind(('127.0.0.1', 12335))     
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
print (s.recv(1024).decode())
service="upload"

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


if(service=="upload"):
  SEPARATOR = "<SEPARATOR>"
  BUFFER_SIZE = 4096
  files=glob.glob("/home/yash/Music/env/*.zip")
  
  for i in range(len(ports)):

    print((len(ports)))
    print(i)
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

elif(service=="download"):
  s1=socket.socket()
  port1 = 60025
  s1.bind(('127.0.0.1', port1))
  s1.listen(5)
 
  c1, addr1 = s1.accept()
   
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

 
print("All sockets connected ")

 

 
  

