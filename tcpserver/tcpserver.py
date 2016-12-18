#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import logging
import struct
from twisted.protocols.basic import Int32StringReceiver

from networkcmddefs import *
from handler import NetworkCmdHandler


class PcTCPProtocol(Int32StringReceiver):

    def __init__(self):
        self.handler = None
        self.net_ver = 0

    def stringReceived(self, data):
        if self.handler is None:
            self.net_ver = struct.unpack('!I', data[:4])[0]
            cmd = struct.unpack('!I', data[4:8])[0]
            logging.debug('network cmd: %s', cmd)

            handler = NetworkCmdHandler.get_handler(cmd)
            self.handler = handler
            handler.bind_protocol(self)
            handler.handle(self.net_ver, data[8:])
        else:
            self.handler.handle_remaining_data(data)

    def connectionLost(self, reason):
        Int32StringReceiver.connectionLost(self, reason)
        if self.handler is not None:
            self.handler.handle_conn_lost(reason)
