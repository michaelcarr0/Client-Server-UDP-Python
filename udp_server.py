# Michael Carr
# MIS 443
# Professor Hayes
# 04/08/2024

import socket, sys
# Imports a socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8085
# Define the IP address and port number of the server
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Creates a socket object for UDP communication
socket_server.bind((SERVER_IP, SERVER_PORT))
print("[*] Server UDP Listening on %s:%d" % (SERVER_IP, SERVER_PORT))
while True:
    data, address = socket_server.recvfrom(4096)
    socket_server.sendto("I am the server accepting connections...".encode(), address)
    data = data.strip()
    print("Message %s received from %s: " % (data, address))
    try:
        response = "Hi %s" % sys.platform
    except Exception as e:
        response = "%s" % sys.exc_info()[0]
    print("Response", response)
    socket_server.sendto(bytes(response, encoding='utf8'), address)
# UDP server listens for messages from clients, responds with an accepted connection, and responds to each message
socket_server.close()

