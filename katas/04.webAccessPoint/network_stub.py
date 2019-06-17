class network:
    AP_IF = "access point"

    class WLAN:

        ssidForTesting = None
        activeForTesting = False
        modeForTesting = None

        def __init__(self, mode):
            self.modeForTesting = mode

        def config(self, essid):
            self.ssidForTesting = essid

        def active(self, activate=None):

            if activate == None:
                return self.activeForTesting
            self.activeForTesting = activate

        def ifconfig(self):
            pass