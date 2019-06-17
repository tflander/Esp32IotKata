try:
    import network
    isTestMode=False
except:
    from network_stub import network
    isTestMode=True

if isTestMode:
    from socket_stub import socket
else:
    import socket

def createAccessPoint(ssid):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.config(essid=ssid)
    ap_if.active(True)
    return ap_if 

def bindHttpLocalHost():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    return s
