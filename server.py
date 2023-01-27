import socket
import base64

# create an IPV4 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
s.bind(("127.0.0.1", 8080))

# listen for incoming connections
s.listen()

# list to store connected clients
clients = []

while True:
    # accept a connection
    conn, addr = s.accept()
    # add the client to the list of connected clients
    clients.append(conn)

    while True:
        try:
            # receive data from the connection
            data = conn.recv(1024)
            decoded_data = data.decode()
            # print the received data
            print("Received:", decoded_data)

            # iterate through the list of connected clients
            for client in clients:
                # send the data to all clients except the sender
                if client != conn:
                    # encode the data in base64 before sending
                    client.sendall(data.encode())
        except:
            # remove the client from the list of connected clients
            clients.remove(conn)
            # close the connection
            conn.close()
            break