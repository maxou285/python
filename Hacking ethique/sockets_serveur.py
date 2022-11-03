# SOCKETS RÉSEAU : SERVEUR
#
# socket
#   bind (ip, port)  127.0.0.1 -> localhost
#   listen
#   accept -> socket / (ip, port)
#   close

# already used

import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print("Attente de connexion sur " + HOST_IP + " port : " + str(HOST_PORT))
connexion_socket, client_adress = s.accept()
print("Connexion établie avec " + str(client_adress))
while True:
    texte_envoye = input("Vous : ")
    connexion_socket.sendall(texte_envoye.encode())
    data_recues = connexion_socket.recv(MAX_DATA_SIZE)
    if not data_recues:
        break
    print("Message : " + data_recues.decode())


s.close()
connexion_socket.close()

