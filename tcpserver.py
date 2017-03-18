# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:39:16 2017

@author: 310251316
"""
import sys
import socket

#create a TCP socket SERVER pgm

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost', 7778)
print('starting up on %s port %s' % server_address)
server_socket.bind(server_address)
server_socket.listen(1)
print("Waiting for connection")
connection, client_address = server_socket.accept()
try:
    while True:
 
        while True:
                data = connection.recv(2000)
                print(data)
                print(str(data.decode('utf-8')))
                print(len(data))
                if len(data)>5:
                    print("Data received :"+ str(data.decode('utf-8')))
                    response = "SERVER DATA:" + str(data.decode('utf-8'))
                    connection.sendall(bytes(response,'utf-8'))
                else:
                    connection.sendall(bytes("connection closing..",'utf-8'))
                    print("no data from clinet")
                    break;
finally:
 connection.close()
 server_socket.close()
            
        
    
    