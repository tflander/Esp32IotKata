import pytest
from onePageHttpServer import OnePageHttpServer
from socket_stub import socket

class TestOnePageHttpServer:

    def webResponse(self):
        return  """
            <html>
                <head>
                    <title>
                        Web Page For Testing
                    </title>
                </head>
                <body>
                    <h1>
                        Web Page For Testing
                    </h1>
                </body>
            </html>
        """

    ## TODO: research Pico Web and decide if can abandon this.
    ## Or be mean and do it anyway
    
    # def test_readsHttpHeaders(self):

    #     def stubWebResponse():
    #         return  "stubbed"

    #     serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     webServer = OnePageHttpServer(stubWebResponse, serverSocket)
    #     webServer.respondtoClient()

    #     cl = serverSocket.incomingClientSocketForTesting
    #     assert cl.bufferOpenedForTesting
    #     assert cl.bufferReadForTesting
