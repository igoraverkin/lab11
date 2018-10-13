import socket
import time
import sys

sock = socket.socket()
attempts = 0 #Попытки подключения

while True:
    if(attempts < 3):
        try:
            sock.connect(('localhost', 9090))
            print("input>", file=sys.stdout)
            f=str(input())
            if f == 'q':
                sock.send(b'Bye!\n')
                sock.close()
            else:
                sock.send(f.encode("utf-8"))
                data = sock.recv(1024)
                udata = data.decode("utf-8")
                print("server> " + udata)
                attempts = 0
        except:
            print('server is not responding... wait 3 seconds...')
            attempts+=1
            time.sleep(3)
    else:
        break
