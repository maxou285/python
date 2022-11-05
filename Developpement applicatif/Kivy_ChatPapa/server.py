import socket
import os
from _thread import *

# -------------------------
# -       CONSTANTES      -
# -------------------------
HOST_IP = ''
HOST_PORT_NUMBER = 2004

# -------------------------------
# -           VARIABLES         -
# -------------------------------

clients_sockets_list = []                                                           # This list will contain all the sockets of each connected client
ThreadCount = 0                                                                     # counts the number of connected Clients

# -------------------------
# -       FUNCTIONS       -
# -------------------------

# The following function handles the reception and sending with a socket connection
# In reality, it's a program that will be executed for each thread 
# A thread is creating each time a Client connects
def multi_threaded_client(connection_socket):
    connection_socket.send(str.encode("You're connected with the server"))          # Welcome message when the client connects
    while True:
        data = connection_socket.recv(2048)                                         # wait until data are received
        response = data.decode('utf-8')                                             # decode data
        if not data:
            break 
        print(response)
        i = 0
        while i < len(clients_sockets_list):
            try:
                clients_sockets_list[i].sendall(str.encode('\n' +"  - " +response))                       # resend the data received to the sender
            except socket.error as e:
                print("Could not send a message to socket: " + str(clients_sockets_list[i]))
                del clients_sockets_list[i]
                continue               # force new loop without executing the rest of the code
            i +=1 
    # exit in case of break
    connection_socket.close()

# -------------------------------
# -       INITITALISATION       -
# -------------------------------

ServerSideSocket = socket.socket()                                              # Create socket and bind to host/port
ServerSideSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    ServerSideSocket.bind((HOST_IP, HOST_PORT_NUMBER))
except socket.error as e:                           # if exception then display it for debug
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)                                                          #5=number of unaccepted connections (need to be checked)

# -------------------------
# -      MAIN PROGRAM     -
# -------------------------

# Loop that:
# . Wait for client connection
# . Creates a separate thread for each connection ()= Client)
while True:
    client_connection_socket, client_address = ServerSideSocket.accept()            # wait until a Client connects and capture the data
    clients_sockets_list.append(client_connection_socket)
    print('Connected to: ' + client_address[0] + ':' + str(client_address[1]))      # address[0]=IP address[1]=port
    start_new_thread(multi_threaded_client, (client_connection_socket, ))           # create a dedicated thread for the client
    ThreadCount += 1                                                                # counts number of clients
    print('Thread Number: ' + str(ThreadCount))

ServerSideSocket.close()
