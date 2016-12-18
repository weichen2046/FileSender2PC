#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import logging
import os
import struct

from storage import StorageManager
from tcpserver.handler import NetworkCmdHandler


class SendFileHandler(NetworkCmdHandler):

    def on_handle(self, net_ver, data):
        self.netver = net_ver
        logging.debug('network data version: %s', self.netver)
        filesize = struct.unpack('!q', data[:8])[0]
        self.filesize = filesize
        self.remain = filesize
        logging.debug('file length: %s', self.filesize)
        self.filename = data[8:]
        logging.debug('file name: %s', self.filename)

        self.outfile = None
        self.outfilepath = None
        if self.filesize > 0 and self.filename:
            sm = StorageManager()
            self.outfilepath = sm.get_store_path(self.filename)
            self.outfile = open(self.outfilepath, 'w')

    def on_remaining_data(self, data):
        self.remain -= len(data)
        self.outfile.write(data)

    def on_conn_lost(self, reason):
        if self.outfile:
            self.outfile.close()

            if self.remain != 0:
                logging.debug('Connection lost but remain(%s) != 0', self.remain)
                os.remove(self.outfilepath)
