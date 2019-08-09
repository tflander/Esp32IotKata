import os

driver = '/dev/cu.SLAB_USBtoUART'
currentFirmware = '~/Downloads/Esp32-20190801-v1.11-187-g00e7fe8ab.bin'

def eraseFirmware():
    os.system('esptool.py --chip esp32 --port ' + driver + ' erase_flash')

def loadFirmware():
    os.system('esptool.py --chip esp32 --port ' + driver + ' --baud 460800 write_flash -z 0x1000 ' + currentFirmware)

loadFirmware()


