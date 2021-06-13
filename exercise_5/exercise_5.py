def exercise_5(inputs): # DO NOT CHANGE THIS LINE
    import sys
    import time
    import socket
    import threading
    import random

    host = "127.0.0.1"
    port = 10001

    class Client:
        def send_msg(self, sckt):
            while True:
                sckt.send(bytes(input(""), 'utf-8'))

        def __init__(self, address):
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sckt.connect((address, 10000))

            iThread = threading.Thread(target=self.send_msg, args=(sckt,))
            iThread.daemon = True
            iThread.start()

            while True:
                data = sckt.recv(1024)
                if not data:
                    break
                if data[0:1] == b'\x11':
                    self.update_peers(data[1:])
                else:
                    print(str(data, 'utf-8'))

        def update_peers(self, peer_data):
            Peer2Peer.peers = str(peer_data, 'utf-8').split(",")[:-1]

    class Server:
        def __init__(self,connections,peers):
            self.connections = connections
            self.peers = peers
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sckt.bind((host, port))
            sckt.listen(5)
            print("Server running...")

            while True:
                c, a = sckt.accept()
                cThread = threading.Thread(target=self.handler, args=(c, a))
                cThread.daemon = True
                cThread.start()
                self.connections.append(c)
                self.peers.append(a[0])
                print(str(a[0]) + ':' + str(a[1]), " connected.")
                self.sender()

        def sender(self):
            p = ""
            for peer in self.peers:
                p = p + peer + ","

            for connection in self.connections:
                connection.send(b'\x11' + bytes(p, 'utf-8'))

        def handler(self, c, a):
            while True:
                data = c.recv(1024)
                for connection in self.connections:
                    connection.send(data)
                if not data:
                    print(str(a[0]) + ':' + str(a[1]), " disconnected.")
                    self.connections.remove(c)
                    self.peers.remove(a[0])
                    c.close()
                    self.sender()
                    break

    class Peer2Peer:
        peers = ['127.0.0.1']

    while True:
        try:
            print("Trying to connect...")
            time.sleep(random.randint(1, 5))
            for peer in Peer2Peer.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(1)
                except:
                    pass

                if random.randint(1, 20) == 1:
                    try:
                        server = Server()
                    except KeyboardInterrupt:
                        sys.exit(1)
                    except:
                        print("Couldn't start the srever...")
        except KeyboardInterrupt:
            sys.exit(1)

    return output       # DO NOT CHANGE THIS LINE
