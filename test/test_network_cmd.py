#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import os
import socket
import struct
import unittest

from networkcmddefs import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class NetworkCmdTester(unittest.TestCase):

    phone_addr = None

    @classmethod
    def setUpClass(cls):
        with open('{}/phone-info.txt'.format(BASE_DIR), 'r') as f:
            phone_ip = f.readline()
            phone_broad_moni_port = int(f.readline())
            cls.phone_addr = (phone_ip, phone_broad_moni_port)

    def setUp(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def tearDown(self):
        self.socket.close()

    def test_cmd_report_pc_monitor_port(self):
        ver = struct.pack('!I', NETWORK_DATA_VERSION)
        # pack cmd
        cmd = struct.pack('!I', CMD_REPORT_PC_MONITOR_PORT)
        # pack port
        l_port = struct.pack('!I', TCP_SERVER_PORT)

        self.socket.sendto(ver + cmd + l_port, self.phone_addr)


if __name__ == '__main__':

    unittest.main()
