import socket
import struct


cords_packer = struct.Struct("ff")


sock = socket.socket()
sock.connect(('10.243.1.98', 5757))
while True:
    bytes = sock.recv(cords_packer.size)
    while len(bytes) < cords_packer.size:
        bytes += sock.recv(cords_packer.size - len(bytes))
    print(cords_packer.unpack(bytes))
