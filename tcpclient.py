# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 01:08:59 2017

@author: 310251316
"""

import sys
import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_adds = ('localhost',7778)
print("connecting to server......")
client_socket.connect(server_adds)
try:
    msg="sending data from machine"
    client_socket.sendall(bytes(msg,'utf-8'))
    data = client_socket.recv(2000);
    print (data)
    print("dtaa received from server:"+ str(data.decode('utf-8')))
    client_socket.sendall(bytes("end",'utf-8'))
    data = client_socket.recv(2000);
    print("dtaa received from server:"+ str(data.decode('utf-8')))
finally:
    client_socket.close()