import socket
import threading


def receiver(*ipPort):
    while True:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s1.bind(ipPort)
        data = s1.recvfrom(1024)
        print(" "*20, data[1][0], " : ", data[0].decode())


def sender(*ipPort):
    while True: 
        data = input()
        s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s2.sendto(data.encode(), ipPort)

IP1 = input("Enter Your IP: ")  
IP1_Port = int(input(f"Enter {IP1} Port: "))

IP2 = input("Enter remote server IP: ")
IP2_port = int(input(f"Enter {IP2} port : "))

rec = threading.Thread(target=receiver,args=(IP1,IP1_Port))
send = threading.Thread(target=sender,args=(IP2,IP2_port))

send.start()
rec.start()
