import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add = "192.168.253.74"
port = 1234
complete = (ip_add, port)
s.bind(complete)
while True:
    msg, addr = s.recvfrom(1024)  
    print(f"Message from {addr}: {msg.decode('ascii')}")
    print(f"Full message data: {msg}")
