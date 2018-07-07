import socket

# HOST is in this case localhost, which is this computer
# PORT is TCP port. port is a communications endpoint on a particular IP address
HOST, PORT = '', 8888

# initialize a socket. SOCK_STREAM for TCP connection
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# reason for bind: we bind host to port so that when we listen, we listen
# to the one we binded (what we are interested in)
listen_socket.bind((HOST, PORT))

# Enable a server to accept connections. system will allow 1 unaccepted
# connections before refusing new connections.
listen_socket.listen(1)

print 'Serving HTTP on port %s ...' % PORT
while True:
    # The socket must be bound to an address and listening for connections.
    # return value: (conn, address)
    #   conn: new socket object usable to send and receive data on the connection
    #   address: the address bound to the socket on the other end of the connection.
    client_connection, client_address = listen_socket.accept()

    # Receive data from the socket.
    # return value: a bytes object representing the data received.
    # parameter: maximum amount of data to be received at once (1024)
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
