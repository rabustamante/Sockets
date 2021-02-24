#!/usr/bin/python3
# client program that connects to server
# Ruben Bustamante CS 4375 02/23/2021

from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 7069))
server_data= []
while True:
    server_data = s.recv(16384)
    if not server_data:
        break
    server_data.append(server_data)
s.close()
response = " ".join(server_data)
print(response)
