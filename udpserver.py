#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import logging
import struct
from twisted.internet.protocol import DatagramProtocol

from networkcmddefs import *


class PcUDPProtocol(DatagramProtocol):

    def datagramReceived(self, data, address):
        if len(data) < 8:
            logging.warn('Udp, data len less then 8 bytes')
            return

        curr_index = 0
        int_size = struct.calcsize('!I')
        # parse version
        version = struct.unpack('!I', data[curr_index:curr_index+int_size])
        if version:
            version = version[0]
        else:
            raise Exception('Can not parse data version')

        logging.debug('version: %s', version)

        # parse command
        curr_index += int_size
        cmd = struct.unpack('!I', data[curr_index:curr_index+int_size])
        if cmd:
            cmd = cmd[0]
        else:
            raise Exception('Can not parse cmd')

        logging.debug('cmd: %s', cmd)

        if cmd == CMD_PHONE_ONLINE:
            # parse listen port
            curr_index += int_size
            list_port = struct.unpack('!I', data[curr_index:curr_index+int_size])
            if list_port:
                list_port = list_port[0]
            else:
                raise Exception('Can not parse listen port')

            logging.debug('listen port: %s', list_port)

            # send our tcp listen port
            # pack data version
            ver = struct.pack('!I', NETWORK_DATA_VERSION)
            # pack cmd
            cmd = struct.pack('!I', CMD_PC_ONLINE)
            # pack port
            l_port = struct.pack('!I', TCP_SERVER_PORT)

            self.transport.write(ver + cmd + l_port, (address[0], list_port))
