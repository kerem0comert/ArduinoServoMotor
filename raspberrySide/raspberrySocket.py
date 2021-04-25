import socket, serial, re, time


WINDOWS_HOST = '192.168.1.41'
RASPBERRY_PORT = 5000
ARDUINO_PORT = '/dev/ttyACM5'
BUFFER_SIZE = 4
BAUD_RATE = 9600
DATA_LENGTH = 6

arduinoSerial = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=0.2)
windowsSocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                                socket.SOCK_STREAM # TCP Protocol
                                )
windowsSocket.connect((WINDOWS_HOST,RASPBERRY_PORT))
message = b'r'

while 1:
    windowsSocket.send(message)
    data = windowsSocket.recv(BUFFER_SIZE).decode()
    print ('Received from server: ', data)
    arduinoSerial.write(data.encode())
    while 1:
        try:
            message = arduinoSerial.readline()
            print('potentValue = ', message)
            #time.sleep(0.1)
            break
        except: pass
    arduinoSerial.flush()

                            
    
windowsSocket.close()

