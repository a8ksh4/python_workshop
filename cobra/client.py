#!/usr/bin/python3

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {0} port {1}'.format(*server_address))
sock.connect(server_address)

try:    
    # Send data
    message = sys.argv[1]
    bin_message = message.encode('ascii')
    print('sending "{}"'.format(message))
    sock.sendall(bin_message)

    # Look for the response
    amount_received = 0
    amount_expected = len(bin_message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "{}"'.format(data.decode('utf-8')))

finally:
    print('closing socket')
    sock.close()
