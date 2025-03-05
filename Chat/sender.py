import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add= "192.168.253.74"
port= 1234
complete=(ip_add,port)
message=input("Enter your msg:")
encode_msgs=message.encode("ascii")
s.sendto(encode_msgs,complete)