import socket
import os
import pickle
from _thread import *
import random

# -------------------------
# -       CONSTANTES      -
# -------------------------
HOST_IP = ''
HOST_PORT_NUMBER = 2004
COLORS = ["#808080","#C0C0C0","#00FFFF","#008080","#008000","#808000","#00FF00","#FF00FF","#FF0000","#F5DEB3",
          "#A52A2A","#8A2BE2","#D2691E","#FF8C00","#00BFFF","#FFD700","#FFA500","#FFC0CB","#DDA0DD","#FA8072","#40E0D0"]

          
# -------------------------------
# -           VARIABLES         -
# -------------------------------

clients_sockets_list = []                                                           # This list will contain all the sockets of each connected client

# -------------------------
# -       FUNCTIONS       -
# -------------------------

# The following function handles the reception and sending with a socket connection
# In reality, it's a program that will be executed for each thread 
# A thread is creating each time a Client connects
def multi_threaded_client(connection_socket, color):
    connection_socket.send(str.encode("[color=#00ff00][b]INFO[/b]: You're connected with the server[/color]"))          # Welcome message when the client connects
    while True:
        data = connection_socket.recv(2048)                                         # wait until data are received
        response = pickle.loads(data)                                               # serialize data on arrival
        if not data:
            break 
        i = 0
        while i < len(clients_sockets_list):
            try:
                clients_sockets_list[i].sendall(str.encode(" - [color=" + color + "]" + response["id"] + "[/color]: " + response["msg"]))                      # resend the data received to the sender
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
    color = COLORS[random.randint(0,len(COLORS)-1)]
    start_new_thread(multi_threaded_client, (client_connection_socket, color ))           # create a dedicated thread for the client

ServerSideSocket.close()
