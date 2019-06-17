# def bindHttpLocalHost():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('', 80))
#     s.listen(5)
#     return s

class socket:

    AF_INET = "IPv4 addresses"
    SOCK_STREAM = "TCP"

    class socket:

        addressTypeForTesting = None
        protocolForTesting = None
        hostAndPortForTesting = None, None
        maxActiveConnectionsForTesting = None
        bufferOpenedForTesting = False
        bufferReadForTesting = False
        incomingClientSocketForTesting = None

        def __init__(self, addrType, protocol):
            self.addressTypeForTesting = addrType
            self.protocolForTesting = protocol

        def bind(self, tuple):
            self.hostAndPortForTesting = tuple

        def listen(self, threads):
            self.maxActiveConnectionsForTesting = threads
            pass

        def accept(self):
            self.incomingClientSocketForTesting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return (self.incomingClientSocketForTesting, "stubbed incoming IP Address")

        def makefile(self, mode, bufsize):
            self.bufferOpenedForTesting = True
            self.bufferReadModeForTesting = mode
            self.bufferReadSizeForTesting = bufsize

            ### sample HTTP Header
            # line b'GET /favicon.ico HTTP/1.1\r\n'
            # line b'Host: 192.168.4.1\r\n'
            # line b'Connection: keep-alive\r\n'
            # line b'Pragma: no-cache\r\n'
            # line b'Cache-Control: no-cache\r\n'
            # line b'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36\r\n'
            # line b'Accept: image/webp,image/apng,image/*,*/*;q=0.8\r\n'
            # line b'Referer: http://192.168.4.1/\r\n'
            # line b'Accept-Encoding: gzip, deflate\r\n'
            # line b'Accept-Language: en-US,en;q=0.9\r\n'
            # line b'\r\n'

            f = open('foo', 'w')
            f.write("testfile")
            f.close
            return open('foo')
