
import App
from Socket import Socket


WINDOWS_HOST = "192.168.1.107"
STREAM_HOST = 'http://192.168.1.33:8081/'
RASPBERRY_PORT = 5000
BAUD_RATE = 9600

def sendData(data, datatp):
    if datatp != 'w': data = data if data > 90 else data + 90
    if(data < 10): data = "00" + str(data)
    elif(data < 100): data = "0" + str(data)
    else:  data = str(data)
    #print("data=", type(data), "datatp=", type(datatp))
    toSend = str(data) + str(datatp)
    print(toSend)
    toSend = str(toSend)
    connection.send(repr(toSend).encode('utf-8'))


socketInstance = Socket(WINDOWS_HOST, RASPBERRY_PORT)

print("Listening...")
connection, address = socketInstance.startListening()
print (f"Connection from: {str(address)}")
app = App(connection)
app.initVideoStream(STREAM_HOST)

while 1:
    app.initGuiElements()
    data = connection.recv(BAUD_RATE).decode()
    if not data: break 
    print(f"From raspberry pi: {str(data)}")
    app.root.mainloop()
connection.close


