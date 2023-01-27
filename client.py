import socket
import threading

def receive(sock):
    while True:
        # receive data from the server
        data = sock.recv(1024)
        # print the received data
        print(data.decode())

def main():
    # create an IPV4 socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect(("127.0.0.1", 8080))

    # ask for a username composed by four letters
    username = input("Enter a username of four letters: ")
    while len(username) != 4:
        username = input("Please enter a valid username of four letters: ")
    # send the username to the server
    s.sendall(username.encode())

    # create a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive, args=(s,))
    receive_thread.start()

    # give the client a prompt to send messages to the server
    while True:
        message = input("You: ")
        # add the username to the beginning of the message
        message = username + " said: " + message
        # send the message to the server
        s.sendall(message.encode())

if __name__ == "__main__":
    main()