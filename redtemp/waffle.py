#!/usr/bin/env python3

import socket
import time

ip = '34.73.195.185'
port = 81

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host_ip = s.getsockname()[0]
s.close()

while(True):
    time.sleep(30)
    try: 
        sock = socket.socket()
        sock.settimeout(3)
        sock.connect((ip, port))
        sock.send(host_ip.encode())
        sock.close()
    except: 
        continue

