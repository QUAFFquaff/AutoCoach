#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 4/29/2020 13:00
# @Author  : Haoyu Lyu
# @File    : test3.py
# @Software: PyCharm
import socket
import time


red = 18
green = 23
yellow = 24


# Define moving functions

options = {"0": RED,
           "1": YELLOW,
           "2": GREEN,
           }

if __name__ == "__main__":

    # Create a Server Socket and wait for a client to connect
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 6666))
    print ("UDPServer Waiting for client on port 6666")

    # Recive data from client and decide which function to call
    while True:
        try:
            dataFromClient, address = server_socket.recvfrom(256)
            print('get data from client: ',dataFromClient)
            print('get data from client ord: ',ord(dataFromClient))
            server_socket.sendto(data,(,6666))
        except Exception as ex:
            print(ex)