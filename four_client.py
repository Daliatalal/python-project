import socket
import threading
host = '127.0.0.1'
send_port = 8888
def send():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, send_port))
        msg = input("Enter your message :   ")
        if msg == "over":
            client.send(msg)
            client.close()
            listen()
        else:
            client.send(b"hello")
def listen():
    print("listenning ...\n")
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((host, recv_port))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        while True:
            data = conn.recv(4096)
            if not data: break
            elif data == "over":
                conn.close()
                serv.close()
                print("closed server and claled send() \n")
                send()
            else:
               print("server : " + data + "\n")
        conn.close()
send()