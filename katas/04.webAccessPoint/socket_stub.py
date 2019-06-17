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

        def __init__(self, addrType, protocol):
            self.addressTypeForTesting = addrType
            self.protocolForTesting = protocol

        def bind(self, tuple):
            self.hostAndPortForTesting = tuple

        def listen(self, threads):
            self.maxActiveConnectionsForTesting = threads
            pass
