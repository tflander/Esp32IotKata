import network
 
def connect():
  ssid = "wifi-iot"
  password =  "getFromWilliam"
 
  station = network.WLAN(network.STA_IF)
 
  if station.isconnected() == True:
      print("Already connected")
      return
 
  station.active(True)
  station.connect(ssid, password)
 
  while station.isconnected() == False:
      pass
 
  print("Connection successful")
  print(station.ifconfig())
