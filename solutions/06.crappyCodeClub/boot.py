try:
    import network, socket
except:
    print('ESP32 modules not found')

def wifiConnect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    print('waiting for connection...')
    while not sta_if.isconnected():
        pass

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    return addr, sta_if.ifconfig()

def apConnect(ssid):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True) 
    ap_if.config(essid=ssid)
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    return addr, ap_if.ifconfig()

def startListener(addr):
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    return s
