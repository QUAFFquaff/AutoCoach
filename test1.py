import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
     data = input("Enter Data :").encode()
     # IPADRESS = "192.168.0.20"
     IPADRESS = "192.168.0.53"
     # 6666 = Number Port
     client_socket.sendto(data, (IPADRESS,6666))
     print ("Sending request")

# except Exception as ex:
#     print ex
#     raw_input()

client_socket.close()