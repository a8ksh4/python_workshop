#!/usr/bin/python3

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {0} port {1}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from {}'.format(client_address))

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16).decode('utf-8')
            print('received "{}"'.format(data))
            if data:
                print('sending data back to the client')
                echo = data.encode('ascii')
                connection.sendall(echo)
            else:
                print('no more data from {}'.format(client_address))
                break
            
    finally:
        # Clean up the connection
        connection.close()

