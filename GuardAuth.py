import socket


s1=socket.socket()
print("socket created")

s1.bind(('127.0.0.1',62000))
print("binded on 62000")

s1.listen(5)
print("Listning")

c, addr = s1.accept()
cred=c.recv(1024).decode()
cred=cred.split()
print("got credentials")
print("checking credentials")

if(cred[0]=="yash" and cred[1]=="yash@123"):
    c.send("yes".encode())
    print("credentials correct")
else:
    c.send("no".encode())
    print("credentials wrong")
