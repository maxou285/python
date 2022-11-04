###########################################################################################
#   Les Imports
###########################################################################################
from kivy.app import App
from kivy.properties import StringProperty
import socket
import time
import os
from _thread import *


class ChatApp(App):
    nick_name = ""
    host_ip = ""
    host_port = ""
    message = StringProperty("Enter your message")
    label_messages = StringProperty("Message")
    ClientMultiSocket = socket.socket()

    # The following function handles the reception of messages from the server
    # and displays them on the client screen
    def display_response_client_thread(self, connection_socket):
        print("Enter function Display response")
        print(connection_socket)
        while True:
            print("Toto ")
            data = connection_socket.recv(2048)                                          # wait until data are received
            print(data)
            if not data:
                break
            print(data.decode('utf-8'))
            self.label_messages += "\n"+ data.decode('utf-8')
        print ('exiting')
        connection_socket.close()

    def on_nickname_validate(self, widget):
        self.nick_name = widget.text
        print(self.nick_name)

    def on_hostip_validate(self, widget):
        self.host_ip = widget.text
        print(self.host_ip)

    def on_hostport_validate(self, widget):
        self.host_port = widget.text
        print(self.host_port)

    def connect_pressed(self):
        print("Nickname: ", self.nick_name, " HOSTIP: ", self.host_ip, ":", self.host_port)
        print('Connecting ...')
        while True:
            try:
                #self.ClientMultiSocket = socket.socket()                                                 # Create client connection socket with the server
                self.ClientMultiSocket.connect((self.host_ip, int(self.host_port)))
            except socket.error as e:
                print(str(e))
                time.sleep(4)
            else:
                print("Connected")
                # Displmay Welcome message
                res = self.ClientMultiSocket.recv(1024)
                print(res.decode('utf-8'))
                # Create a listening thread that will listen for data from the server
                # for all the other messages coming from the server
                start_new_thread(self.display_response_client_thread, (self.ClientMultiSocket, ))           
                break
        
    def send_message(self, widget):
        print("Send Message")
        self.message = widget.text
        print(self.message)
        self.ClientMultiSocket.sendall(str.encode(self.nick_name + ": " + self.message))


ChatApp().run()
