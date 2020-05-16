import socket, serial


WINDOWS_HOST = '192.168.1.107'
RASPBERRY_PORT = 5000
ARDUINO_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

ser = serial.Serial(ARDUINO_PORT, BAUD_RATE)
mySocket = socket.socket()
mySocket.connect((WINDOWS_HOST,RASPBERRY_PORT))
message = 'ready'

while 1:
    mySocket.send(message.encode()) #acknowledge each time we're ready to recieve more instructions
    data = mySocket.recv(BAUD_RATE).decode()
    print ('Received from server: ', data)
    ser.write(data.encode()) #serialize the data
mySocket.close()
 

