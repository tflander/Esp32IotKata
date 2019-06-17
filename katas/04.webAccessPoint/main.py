from connectAccessPoint import createAccessPoint, bindHttpLocalHost
import socket

ap = createAccessPoint("ESP32 Network")
print(ap.ifconfig()) # address is always 192.168.4.1 (I think)
serverSocket = bindHttpLocalHost()

html = """<!DOCTYPE html>
<html>
    <head> <title>Hello ESP32</title> </head>
    <body> <h1>Hello ESP32</h1>
        <p>This page is coming from a web server running on an ESP32 chip</p>
    </body>
</html>
"""

def clearSocket(cl):
    cl_file = cl.makefile('rwb', 0) # type is socket
    while True:
        line = cl_file.readline()
        print("line", line.decode('utf-8'))
        if not line or line == b'\r\n':
            break

while True:
    cl, addr = serverSocket.accept()
    print('client connected from', addr)

    clearSocket(cl)

    cl.send(html)
    cl.close()
