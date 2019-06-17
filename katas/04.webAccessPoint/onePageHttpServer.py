
def clearSocket(clientSocket):
    cl_file = clientSocket.makefile('rwb', 0)  # TODO: does the buffer really need to be writable?
    incomingData = cl_file.readlines()
    return incomingData

class OnePageHttpServer:

    fGetWebResponseHtml = None
    serverSocket = None

    def __init__(self, fGetWebResponseHtml, serverSocket):
        self.fGetWebResponseHtml = fGetWebResponseHtml
        self.serverSocket = serverSocket

    def respondtoClient(self):
        clientSocket, addr = self.serverSocket.accept()
        print('client connected from', addr)  ## TODO: get rid of side-effect
        incomingData = clearSocket(clientSocket)
        print("client incoming data", incomingData)

        # clientSocket.send(html)
        # clientSocket.close()


