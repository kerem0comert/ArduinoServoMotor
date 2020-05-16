import socket, serial
from time import sleep
 
def Main():
    host = '192.168.1.107'
    port = 5000
    arduinoPort = '/dev/ttyACM0'
    bandRate = 9600
        
    mySocket = socket.socket()
    mySocket.connect((host,port))
    message = 'ready'
    ser = serial.Serial(arduinoPort, bandRate)
        
    while True:
        mySocket.send(message.encode())
        data = mySocket.recv(bandRate).decode()
        print ('Received from server: ', data)

        ser.write(data.encode()) #serialize the data
        

    mySocket.close()
 
if __name__ == '__main__':
    Main()
