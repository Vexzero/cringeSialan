#tool gabungan dari beberapa tool
import color
import subprocess
import getpass
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import hashlib
import time
try:
    os.system("cls||clear")
    def halo():
        sys.stdout.write(color.CYAN+"""
                         /$$                 /$$       /$$$$$$$$                  /$$
                        |__/                | $$      |__  $$__/                 | $$
 /$$  /$$  /$$  /$$$$$$  /$$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$
| $$ | $$ | $$ /$$__  $$| $$ /$$__  $$ /$$__  $$         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/
| $$ | $$ | $$| $$$$$$$$| $$| $$  \__/| $$  | $$         | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$
| $$ | $$ | $$| $$_____/| $$| $$      | $$  | $$         | $$| $$  | $$| $$  | $$| $$ \____  $$
|  $$$$$/$$$$/|  $$$$$$$| $$| $$      |  $$$$$$$         | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/
 \_____/\___/  \_______/|__/|__/       \_______/         |__/ \______/  \______/ |__/|_______/
 """+color.END)
    halo()
    text = color.FAIL+"Available tools in this program"+color.END
    for a in text:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.01)
    def new():
        print()
        sys.stdout.write(color.CYAN+"""
----------------------------------------
1.gmail send				           
2.hashMachine				                   
3.passwordMachine			                 
4.show wifi pw	       *(windows only)*
5.ec to de / de to en 			           
99.exit				                         
					                             
-----------------------(AUTHOR : VEEX) -
"""+color.END)
    new()
    print()
    stop = False
    i = 1
    while(not stop):
        masukkan = input(color.YELLOW+"[?] "+color.CYAN)
        i += 1
        if masukkan == "1":
            try:
                sender = input("Email : ")
                pwd = getpass.getpass("password : ")
                to = input("to : ")
                subject = input("Subject : ")
                body = input("message : ")
                message = MIMEMultipart()
                message['from'] = sender
                message['to'] = to
                message['subject'] = subject
                message.attach(MIMEText(body,'plain'))
                text = message.as_string()
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login(sender,pwd)
                server.sendmail(sender,to,text)
                server.close()
                print("Done....")
            except smtplib.SMTPAuthenticationError:
                print("make sure the password and email are true")
                print("make sure that you was enable the 'les security' on gmail")
        elif masukkan == "2":
            print("available : {}".format(",".join(sorted(hashlib.algorithms_available))))
            print()
            print("guaranteed : {}".format(",".join(sorted(hashlib.algorithms_guaranteed))))
            print()
            print()
            data = input("text you want to be encrypt : ")
            hashname = input("hashmname : ")
            h = hashlib.new(hashname)
            h.update(data.encode("utf-8"))
            print("hexdigest = {}".format(h.hexdigest()))
            print()
            print("digest = {}".format(h.digest()))
        elif masukkan == "3":
            md5pw = input("hash : ")
            md5file = input("file location : ")
            nama_hash = input("type of hash : ")
            counter = 1
            try:
                md5file = open(md5file,"r")
            except:
                print("file not found")
                quit()
            for password in md5file:
                pwd = hashlib.new(nama_hash,password.strip().encode("utf-8")).hexdigest()
                start = time.time()
                print("proses.......%d : %s" % (counter,password.strip()))
                counter += 1
                end = time.time()
                total = end-start
                stop = False

                if pwd == md5pw:
                    print("=========================")
                    print("in pw nya : %s" % password)
                    print("time : ",total,"sec")
                    print("=========================")
                    break
                else:
                    print("bukan")
                    print("pass nggk ada")
        elif masukkan == "clear" :
            os.system("cls||clear")
            halo()
            new()
            print()
        elif masukkan == "sysinfo":
            os.system("systeminfo")
        elif masukkan == "ifconfig":
            os.system("ifconfig")
        elif masukkan == "4":
            subprocess.call(['netsh','wlan','show','profiles'])
            pilih = input("==> ")
            subprocess.call(['netsh','wlan','show','profiles',pilih,'key=clear'])
        elif masukkan == "5":
            import time
            text = input("text : ")
            space = 26
            count = 26
            encrypt = ""
            for i in range(count):
                start = time.time()
                count -= 1
                space -=1
                encrypt = ""
                for data in text:
                    if data.islower():
                        unicode = ord(data)
                        index = ord(data) - ord("a")
                        new_index = (index + space) % 26
                        new_unicode = new_index + ord("a")
                        hasil = chr(new_unicode)
                        encrypt = encrypt + hasil
                    elif data.isupper():
                        unicode = ord(data)
                        index = ord(data) - ord("A")
                        new_index = (index + space) %26
                        new_unicode = new_index + ord("A")
                        hasil = chr(new_unicode)
                        encrypt = encrypt + hasil
                    else:
                        encrypt += data
                print(color.CYAN+"wordlist {}\t:".format(count),color.YELLOW+encrypt+color.END)
                selsai = time.time()
        elif masukkan == "ping":
            target = input("to : ")
            subprocess.call(['ping',target])
        elif masukkan == "help":
            print(color.BOLD+"udah jelas bro tinggal pencet\nabis itu copy paste\n ini tool gampang"+color.END)
        elif masukkan == "99":
            print("bye...")
            stop = True
        else:
            print(color.RED+"[X]perintah belum ada[X]"+color.END)
except KeyboardInterrupt:
    print("cancelled")
except:
    print("cancelled")
