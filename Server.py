import socket
import threading
from Calculator import calc

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(2)
        while True:
            client, address = self.sock.accept()
            print('connected: ', address)
            #client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    uData=data.decode("utf-8")
                    print("client", address[1], '>', uData)
                    counts= str(uData)
                    f=str(calc.calc(counts))
                    client.send(f.encode("utf-8"))
                else:
                    raise error("Client", address[1], "disconnected")
            except:
                print("client", address[1], "discontected")
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = "9090"
        print("Port is",port_num)
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()