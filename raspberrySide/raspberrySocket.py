import socket, serial

WINDOWS_HOST = "192.168.1.41"
RASPBERRY_PORT = 5000
ARDUINO_PORT = "/dev/ttyACM5"
BUFFER_SIZE = 4
BAUD_RATE = 9600
DATA_LENGTH = 6

arduino_serial = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=0.2)
windows_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM  # for ipv4 communiciation  # TCP Protocol
)
windows_socket.connect((WINDOWS_HOST, RASPBERRY_PORT))
message = b"r"

while 1:
    windows_socket.send(message)
    data = windows_socket.recv(BUFFER_SIZE).decode()
    print(f"Received from server: {data}")
    arduino_serial.write(data.encode())
    while 1:
        try:
            message = arduino_serial.readline()
            print("potentValue={message}")
            # time.sleep(0.1)
            break
        except:
            pass
    arduino_serial.flush()

windows_socket.close()
