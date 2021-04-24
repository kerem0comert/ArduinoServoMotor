import socket, serial, re, time


WINDOWS_HOST = '192.168.1.41'
RASPBERRY_PORT = 5000
ARDUINO_PORT = '/dev/ttyACM1'
BAUD_RATE = 4
DATA_LENGTH = 6

arduinoSerial = serial.Serial(ARDUINO_PORT, BAUD_RATE)
windowsSocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                                socket.SOCK_STREAM # TCP Protocol
                                )
windowsSocket.connect((WINDOWS_HOST,RASPBERRY_PORT))
message = 'ready'

while 1:
    windowsSocket.send(message.encode()) #acknowledge each time we're ready to recieve more instructions
    data = windowsSocket.recv(BAUD_RATE).decode()
    print ('Received from server: ', data)
    arduinoSerial.write(data.encode())



    """potentValue = arduinoSerial.read(4)
    print('potentValue = ', potentValue)"""
    
windowsSocket.close()

