from flask import Flask, render_template, Response, request, redirect, url_for
from flask import Request
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
 
import subprocess
import socket 
import time
import tqdm
import os
import glob
import file
 
 

print("Y001")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')




@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        
        s1=socket.socket()
        s1.connect(('127.0.0.1',62000))
        user=(form.username.data)
        username=str(form.username.data)
        password=str(form.password.data)
        creden=username+" "+password
        s1.send(creden.encode())
        permission=s1.recv(1024).decode()
        if(permission=="yes"):
            s1.close()
            return redirect(url_for('profile'))
        else:
            s1.close()
            return render_template('index.html')

             
    else:
         
        return render_template('login.html',form=form)
            


@app.route('/logout', methods=['GET', 'POST'])
def logout():
     
    return redirect(url_for('home'))


@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/history')
def history():
    return render_template('index2.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/pasd', methods=['GET', 'POST'])
def pasd():
    print("pass 1")
     
    print("pass 2")
    text="sysgrg"
    print(text)
    getLocation =  subprocess.Popen("locate "+str(text), shell=True, stdout=subprocess.PIPE).stdout
    location =  getLocation.read()
    locationD=location.decode()
    locationD1=locationD.splitlines()
    filelocation=locationD1[0]
    print(filelocation)
    os.system("cp "+str(filelocation)+" /home/yash/Videos/Downloads/")
      
    return render_template('download.html')


@app.route('/success', methods = ['POST'])  
def success():  
    print("success 1")
    if request.method == 'POST': 
        print("success 2") 
        f = request.files['file']
        f.save(f.filename)
        global k
        k=str(f.filename)
        print(f)
        print(type(f))
        print("3") 
        # f.save(f.filename) 
        print("4") 
         
        # print(f.filename)
        # print(type(f.filename))
        file.splitting(f.filename)

        return render_template("upload.html", name = f.filename)  

@app.route("/SomeFunction",methods=['GET', 'POST']) 
def SomeFunction():
    
    print("Yoo3")
     
    print("yes")
    s = socket.socket()   
    s.bind(('127.0.0.1', 12335)) 
    port=12345
    s.connect(('127.0.0.1', port))
    print (s.recv(1024).decode())
    service="upload"
    cred="yash yash123 192.168.22.3 "+service
    print("Message initialized")
    s.send(cred.encode())
    print("Message sent")
    Allports = s.recv(1024).decode()
    print(Allports)
    print("Message receved")
    s.close()  
    credF="Yash yash123 IP_address"
    ports=Allports.split()
    i=0
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    files=glob.glob("/home/yash/Downloads/Splits/k/*.zip")
    for i in range(len(ports)):
        filename=files[i]
        filename=str(filename)
        filesize = os.path.getsize(filename)
        s1 = socket.socket()
        s1.connect(('127.0.0.1',int(ports[i])))
        s1.send("hloo".encode())
        rec=s1.recv(1024).decode()
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
         
    return "Nothing"
         
    
     
 
app.run(debug=True)