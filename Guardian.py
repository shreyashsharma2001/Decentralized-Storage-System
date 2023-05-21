import socket            
import mariadb
import time
import sys
 
s = socket.socket()        
print ("Socket successfully created")
  
port = 12345               
 
 
s.bind(('127.0.0.1', port))        
print ("socket binded to %s" %(port))
  
s.listen(5)    
print ("socket is listening")           
 
# while True:
 
# Establish connection with client.
c, addr = s.accept()    
print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type.
c.send('Connected with guardian'.encode())
print("G1")

  #print (s.recv(1024).decode())

 
 
# Instance the Fernet class with the key
 
 
  
decCred1 =c.recv(1024).decode()
 
decCred=decCred1.split()
print(decCred)
cred="Yash yash@123 192.168.22.3"
Skey=" Secret_key"
cred2="IP_address Ports"
decCred1=decCred1+Skey
try:
    conn = mariadb.connect(
        user="yash",
        password="yash123",
        host="127.0.0.1",
        port=3306,
        database="Guardian1"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
print(type((decCred[0])))
sql= "select Password from Authentication where Username=\'"+str(decCred[0])+"\'"
data=(decCred[0])
cur.execute(sql )                                                
output = cur.fetchone()
print(decCred[1])
print(output[0])
 
if(decCred[1]==output[0]):


    print("Key initialized")
	 
  # Close the connection with the client
  

    

    if(decCred[3]=="upload"):
      ipAdd=["127.0.0.1","127.0.0.1","127.0.0.1"]
      ports=[12346,12347,12348]
      portsrep=[61001,61002,61003,61004,61005,61006]
      i=0
      j=0
      for i in range(len(ports)):
          print((len(ports)))
          s1 = socket.socket() 
          portrep=str(portsrep[j])+" "+str(portsrep[j+1])
          print("server "+str(i)+" on")
          s1.connect((ipAdd[i],ports[i]))
          s1.send(portrep.encode())
          s1.recv(1024).decode()

          s1.send(decCred1.encode())
          s1.recv(1024).decode()
           
         
   

         
          s1.close()
          i=i+1
          j=j+2
        
          time.sleep(2)
    elif(decCred1[3]=="download"):
      print("This is download")
     
 
else:
	print("no")

cred1="60001 60002 60003"
c.send(cred1.encode())
  
 


 

