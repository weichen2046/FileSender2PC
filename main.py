#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import socket
import struct

from networkcmddefs import *


if __name__ == '__main__':

    host = ''
    port = 4555

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.bind((host, port))

    data, addr = s.recvfrom(4096)
    print 'recv broadcast,', 'addr:', addr

    curr_index = 0
    int_size = struct.calcsize('!I')
    # parse version
    version = struct.unpack('!I', data[curr_index:curr_index+int_size])
    if version:
        version = version[0]
    else:
        raise Exception('Can not parse data version')

    print 'version:', version

    # parse command
    curr_index += int_size
    cmd = struct.unpack('!I', data[curr_index:curr_index+int_size])
    if cmd:
        cmd = cmd[0]
    else:
        raise Exception('Can not parse cmd')

    print 'cmd:', cmd

    if cmd == CMD_REPORT_PHONE_BROAD_MONITOR_PORT:
        # parse listen port
        curr_index += int_size
        list_port = struct.unpack('!I', data[curr_index:curr_index+int_size])
        if list_port:
            list_port = list_port[0]
        else:
            raise Exception('Can not parse listen port')

        print 'listen port:', list_port

        # send our tcp listen port
        # pack data version
        ver = struct.pack('!I', NETWORK_DATA_VERSION)
        # pack cmd
        cmd = struct.pack('!I', CMD_REPORT_PC_MONITOR_PORT)
        # pack port
        l_port = struct.pack('!I', TCP_SERVER_PORT)

        s.sendto(ver + cmd + l_port, (addr[0], list_port))

    s.close()
