###########################################################################################
#   Les Imports
###########################################################################################
import os
import socket
import time
from threading import main_thread

from _thread import *
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.app import MDApp
import random


class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
    nick_name = "c"
    host_ip = ""
    host_port = ""
    message = StringProperty("")
    label_messages = StringProperty("")
    ClientMultiSocket = socket.socket()

    # The following function handles the reception of messages from the server
    # and displays them on the client screen
    def display_response_client_thread(self, connection_socket):
        print(connection_socket)
        while True:
            data = connection_socket.recv(2048)                                          # wait until data are received
            if not data:
                break
            self.label_messages += "\n"+ data.decode('utf-8')
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

    def connect_with_server(self,connection_socket):
        while True:
            try:
                connection_socket = socket.socket()                                                 # Create client connection socket with the server
                connection_socket.connect((self.host_ip, int(self.host_port)))
            except socket.error as e:
                print(str(e))
                print("Reconnecting...")
                #self.label_messages += "\n"+ "Reconnecting..."
                Clock.schedule_once(self.update, -5)
                #Clock.schedule_once(self.update)
                #start_new_thread(self.update, (connection_socket, ))
                Clock.tick()
                time.sleep(1)
            else:
                print("Connected")
                self.ClientMultiSocket = connection_socket
                # Display Welcome message
                res = connection_socket.recv(1024)
                print(res.decode('utf-8'))
                # Create a listening thread that will listen for data from the server
                # for all the other messages coming from the server
                start_new_thread(self.display_response_client_thread, (connection_socket, ))           
                break

    def update(self, dt):
        print("Reconnecting...")
        self.label_messages += "\n"+ "Reconnecting..."
    def connect_pressed(self):
        print('Connecting ...')
        self.connect_with_server(self.ClientMultiSocket)
    
    def send_message(self, text):
        print("Send Message")
        self.message = text
        print(self.message)
        try:
            self.ClientMultiSocket.sendall(str.encode(self.nick_name + ": " + self.message))
        except:
            print("exception")
            self.connect_pressed()
        self.message = ""


ChatApp().run()
