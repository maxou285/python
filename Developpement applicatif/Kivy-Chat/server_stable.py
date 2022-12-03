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

          
# -------------------------------
# -           VARIABLES         -
# -------------------------------

clients_sockets_list = []                                                           # This list will contain all the sockets of each connected client
client_list_dict = {"ids": [] , "type": "client_ref"}
#client_list_dict = []
message_dict = {"ids":[], "msg": ""}
# -------------------------
# -       FUNCTIONS       -
# -------------------------

# The following function handles the reception and sending with a socket connection
# In reality, it's a program that will be executed for each thread 
# A thread is creating each time a Client connects
def multi_threaded_client(connection_socket, color):
    connection_socket.send(str.encode("[color=#00ff00][b]INFO[/b]: You're connected with the server[/color]"))          # Welcome message when the client connects
    data_on_connect = connection_socket.recv(2048)
    user_id = pickle.loads(data_on_connect)
    message_dict["ids"].append(user_id["id"])
    message_dict["msg"] = "[color=#ff7f00]"+ user_id["id"]+ " vient de se connecter au serveur[/color]"
    print(message_dict)
    send_to_all(message_dict)                                                                        # Welcome message
    while True:
        data = connection_socket.recv(2048)
        response = pickle.loads(data)
        print(response)
        if response["type"] == "Disconecting":
            message_dict["msg"] = "[color=#ff7f00]"+ user_id["id"]+ " vient de se déconnecter du serveur[/color]"
            send_to_all(message_dict)                                                                # Disconecting
            print(message_dict)
            break
        message_dict["msg"] = " - [color=" + color + "]" + response["id"] + "[/color]: " + response["msg"]
        send_to_all(message_dict)                                                                     # Send message
    # exit in case of break
    connection_socket.close()

def send_to_all(dict):
    i = 0
    while i < len(clients_sockets_list):
        try:
            clients_sockets_list[i].sendall(pickle.dumps(dict))
            print(message_dict)
        except socket.error as e:
            print("Could not send a message to socket: " + str(clients_sockets_list[i]))
            del clients_sockets_list[i]
            continue               # force new loop without executing the rest of the code
        i +=1 

def color_choose():
    color = str(hex(random.randint(0,255)))
    color = color[2:]
    if int(color,16) < 10:
        color = "0" + color
    return color


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
    #color = COLORS[random.randint(0,len(COLORS)-1)]
    red = color_choose()
    green = color_choose()
    blue = color_choose()
    color = "#" + red + green + blue
    print(color)
    start_new_thread(multi_threaded_client, (client_connection_socket, color ))           # create a dedicated thread for the client

ServerSideSocket.close()
