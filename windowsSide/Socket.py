from socket import socket, AF_INET, SOCK_STREAM

class Socket:
    def __init__(self, WINDOWS_HOST, RASPBERRY_PORT):
        self.mySocket = socket(
                                AF_INET, #for ipv4 communiciation
                                SOCK_STREAM # TCP Protocol
                                )
        self.mySocket.bind((WINDOWS_HOST, RASPBERRY_PORT))
        
    def startListening(self): 
        self.mySocket.listen(1)
        return self.mySocket.accept()
    
    def stopListening(self): self.mySocket.close()