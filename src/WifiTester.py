import socket
import json
import struct
import binascii
import datetime

HOST = '192.168.4.2'  # Standard loopback interface address (localhost)
PORT = 145       # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()

i = 0
while i < 1600:
    data = conn.recv(33)
    if i == 0:
        start = datetime.datetime.now()
    try:
        # print(struct.unpack('ffff', '00'.decode('hex') + data[2:5] + '00'.decode('hex') + data[5:8] + '00'.decode('hex') + data[8:11] + '00'.decode('hex') + data[11:14]))
        ans = struct.unpack('B', data[1])
        i += 1
    except:
        pass
print datetime.datetime.now() - start