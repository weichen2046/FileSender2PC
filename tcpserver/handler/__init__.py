#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


from networkcmddefs import *


class NetworkCmdHandler(object):

    def bind_protocol(self, protocol):
        self.protocol = protocol

    def handle(self, net_ver, data):
        self.on_handle(net_ver, data)

    def on_handle(self, net_ver, data):
        pass

    def handle_remaining_data(self, data):
        self.on_remaining_data(data)

    def on_remaining_data(self, data):
        pass

    def handle_raw_data(self, data):
        self.on_raw_data(data)

    def on_raw_data(self, data):
        pass

    def handle_conn_lost(self, reason):
        self.on_conn_lost(reason)

    def on_conn_lost(self, reason):
        pass

    @staticmethod
    def get_handler(cmd):
        if cmd == CMD_SEND_FILE:
            from sendfilehandler import SendFileHandler
            return SendFileHandler()

        return NetworkCmdHandler()
