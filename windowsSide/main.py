
from windowsSide.App import App
from windowsSide.Socket import Socket

WINDOWS_HOST = "192.168.1.107"
STREAM_HOST = 'http://192.168.1.33:8081/'
RASPBERRY_PORT = 5000
BAUD_RATE = 9600

app = App()
socketInstance = Socket(WINDOWS_HOST, RASPBERRY_PORT)

print("Listening...")
socketInstance.startListening()
print (f"Connection from: {str(socketInstance.address)}")

app.initVideoStream(STREAM_HOST)

while 1:
    data = socketInstance.connection.recv(BAUD_RATE).decode()
    if not data: break 
    print(f"From raspberry pi: {str(data)}")
    app.initGuiElements(socketInstance)
    app.root.mainloop()
socketInstance.stopListening()


