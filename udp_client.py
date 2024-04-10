import socket
# Imports a socket. Sockets are an endpoint that receives data.
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8085
# Defines the IP address and port number of the server.
address = (SERVER_IP, SERVER_PORT)
# Creates tuple 'address' containing the server's IP address and port number.
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Creates a UDP socket object using the socket() function from the socket module.
# AF_INET indicates the address family of IPv4, and SOCK_DGRAM specifies that this is a UDP socket.
while True:
    message = input("Enter your name and message > ")
    if message == "quit":
        break
    socket_client.sendto(bytes(message, encoding='utf8'), address)
    response_server, addr = socket_client.recvfrom(4096)
    print("Response from the server => %s" % response_server)
socket_client.close()
