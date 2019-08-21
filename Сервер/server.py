import requests
import socket
import struct
import time

last_message_id = 0

sock = socket.socket()
port = 5458
sock.bind(('10.91.37.228', port))
sock.listen(1)
conn, addr = sock.accept()
print("connected")
cords_packer = struct.Struct("ff")
status_packer = struct.Struct('h')

for i in requests.get("https://api.telegram.org/bot638873335:AAFNAzhthrOh0zne5BkEqi5NkXay6dZzP1Y/getUpdates").json()['result']:
    id = i['message']["message_id"]
    if id > last_message_id:
        last_message_id = id
        cords = i['message']["text"].split()
        print(cords)
        for i in range(len(cords)):
            cords[i] = float(cords[i])
        conn.send(cords_packer.pack(cords[0], cords[1]))
        break
print(status_packer.unpack(conn.recv(status_packer.size)))
