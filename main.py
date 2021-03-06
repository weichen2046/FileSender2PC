#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import logging
import logging.config
import os
import socket
import struct
from twisted.internet import reactor, protocol

import settings
from networkcmddefs import *
from tcpserver.tcpserver import PcTCPProtocol
from udpserver import PcUDPProtocol


def init_logging():
    log_dir = os.path.join(settings.BASE_DIR, 'logs')
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    logging.config.dictConfig(settings.LOGGING)


def run():

    host = ''
    port = 4555

    reactor.listenUDP(port, PcUDPProtocol())

    factory = protocol.ServerFactory()
    factory.protocol = PcTCPProtocol
    reactor.listenTCP(TCP_SERVER_PORT, factory)

    reactor.run()


if __name__ == '__main__':


    init_logging()

    logging.debug('pc online...')

    run()

    logging.debug('pc offline...')
