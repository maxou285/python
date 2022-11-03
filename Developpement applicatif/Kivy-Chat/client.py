import socket
import time
import os
from _thread import *

# -------------------------
# -       CONSTANTES      -
# -------------------------
HOST_IP = '127.0.0.1'
HOST_PORT_NUMBER = 2004

# -------------------------
# -       FUNCTIONS       -
# -------------------------

# The following function handles the reception of messages from the server
# and displays them on the client screen
def display_response_client_thread(connection_socket):
    cpt = 0
    while True:
        cpt += 1
        data = connection_socket.recv(2048)                                          # wait until data are received
        if not data:
            break
        print(data.decode('utf-8'))
    print ('exiting')
    connection_socket.close()

# -------------------------------
# -       INITITALISATION       -
# -------------------------------
user_name = input("Enter your name: ")

print('Connecting ...')
while True:
    try:
        ClientMultiSocket = socket.socket()                                                 # Create client connection socket with the server
        ClientMultiSocket.connect((HOST_IP, HOST_PORT_NUMBER))
    except socket.error as e:
        print(str(e))
        time.sleep(4)
    else:
        break

# -------------------------
# -      MAIN PROGRAM     -
# -------------------------
# Loop that:
# . receive data from the server
# . wait input from the user to send to the server

# Displmay Welcome message
res = ClientMultiSocket.recv(1024)
print(res.decode('utf-8'))

# Create a listening thread that will listen for data from the server
# for all the other messages coming from the server
start_new_thread(display_response_client_thread, (ClientMultiSocket, ))           

while True:
    Input = input(user_name + ': ')
    if not Input:
        break
    ClientMultiSocket.send(str.encode(user_name + ": " + Input))
    time.sleep(1/10)

# EXIT

