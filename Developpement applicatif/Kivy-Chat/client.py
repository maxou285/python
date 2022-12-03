###########################################################################################
#   Les Imports
###########################################################################################
import os
import pickle
import random
import socket
import time
from multiprocessing.process import active_children
from threading import main_thread

from setuptools.command import test

from _thread import *
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text.markup import MarkupLabel
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp

dingfile = os.path.join("ding.wav")
class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        print(self.root.ids)
       
    nick_name = ""
    host_ip = "127.0.0.1"
    host_port = "2004"
    message = StringProperty("")
    label_messages = StringProperty("")
    ClientMultiSocket = socket.socket()
    users_ids = StringProperty("")
    slider_on = StringProperty("True")
    #test = StringProperty("[color=ff0000]Host Ip [/color]")

    # The following function handles the reception of messages from the server
    # and displays them on the client screen
    def display_response_client_thread(self, connection_socket):
        global data_decode
        while True:
            data = connection_socket.recv(2048)                                          # wait until data are received
            data_decode = pickle.loads(data)
            print(data_decode)
            self.label_messages += "\n"+ data_decode["msg"]
            print(self.slider_on)
            if not data_decode["msg"][18:int(18+len(self.nick_name))] == self.nick_name:
                if self.slider_on == "True":
                    os.system("afplay " + dingfile)
            self.users_ids = ""
            for client in data_decode["ids"]:
                self.users_ids += "\n"+"[b] - "+client+"[/b]"

    def on_nickname_validate(self, widget):
        self.nick_name = widget.text
        print(self.nick_name)

    def switch_on(self, widget):
        print("Switched on ")
        self.slider_on = str(widget.active)
        print(widget.active)

    def on_hostip_validate(self, widget):
        self.host_ip = widget.text
        print(self.host_ip)

    def on_hostport_validate(self, widget):
        self.host_port = widget.text
        print(self.host_port)

    def disconnect_pressed(self):
        print("Disconnecting..........")
        dict = {"id": self.nick_name, "type": "Disconecting"}
        try:
            self.ClientMultiSocket.sendall(pickle.dumps(dict))
            print("send")
        except:
            print("echec")
        time.sleep(2)
        self.ClientMultiSocket.close()
        self.label_messages += "[color=#00ff00]\n[b]INFO[/b]: You succesfully disconnected[/color]"

    def connect_pressed(self):
        print('Connecting ...')
        try:
            self.ClientMultiSocket.close()
            self.ClientMultiSocket = socket.socket()                                                 # Create client connection socket with the server
            self.ClientMultiSocket.connect((self.host_ip, int(self.host_port)))
        except ValueError:
            self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: Provide Nickname, Server IP and port[/color]"
        except socket.error as e:
            print(str(e))
            self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: Server offline ...[/color]"
        else:
            print("Connected")
            self.ClientMultiSocket = self.ClientMultiSocket
            # Display Welcome message
            res = self.ClientMultiSocket.recv(1024)
            dict = {"id": self.nick_name, "type": "message"}
            self.ClientMultiSocket.sendall(pickle.dumps(dict))
            self.label_messages += "\n " + res.decode('utf-8')
            # Create a listening thread that will listen for data from the server
            # for all the other messages coming from the server
            start_new_thread(self.display_response_client_thread, (self.ClientMultiSocket, ))
    
    def send_message(self, text):
        self.message = text
        try:
            dict = {"id": self.nick_name, "msg": self.message, "type": "message"}
            self.ClientMultiSocket.sendall(pickle.dumps(dict))
        except socket.error as e:
            if (e.errno == 57) or (e.errno == 9):
                self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: You must connect with the server[/color]"
            if e.errno == 61:
                self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: Server offline[/color]"
            print(str(e))
        self.message = ""
    

ChatApp().run()
ChatApp().disconnect_pressed()