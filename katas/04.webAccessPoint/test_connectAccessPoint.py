import pytest
from mock import Mock, patch
from connectAccessPoint import createAccessPoint, bindHttpLocalHost
from network_stub import network
from socket_stub import socket

class TestCreateAccessPoint():

    def test_verifyApMode(self):
        ap = createAccessPoint('ssid')
        assert ap.modeForTesting == network.AP_IF

    def test_serviceSetIdentifierParameterUsedForTheNetworkName(self):
        ap = createAccessPoint('ssid')
        assert ap.ssidForTesting == 'ssid'

    def test_networkIsActivated(self):
        ap = createAccessPoint('ssid')
        assert ap.activeForTesting

class TestbindHttpLocalHost():

    def test_verifyIPv4Addresses(self):
        s = bindHttpLocalHost()
        assert s.addressTypeForTesting == socket.AF_INET

    def test_verifyTcpProtocol(self):
        s = bindHttpLocalHost()
        assert s.protocolForTesting == socket.SOCK_STREAM

    def test_verifyHostAndPort(self):
        s = bindHttpLocalHost()
        host, port = s.hostAndPortForTesting
        assert host == ''
        assert port == 80

    def test_verifyUpToFiveActiveConnections(self):
        s = bindHttpLocalHost()
        assert s.maxActiveConnectionsForTesting == 5

