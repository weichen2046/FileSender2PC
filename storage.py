#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import os
import datetime


class StorageManager(object):

    def get_store_dir(self):
        user_home = os.path.expanduser('~')
        work_home = os.path.join(user_home, 'filesender')

        now = datetime.datetime.now()

        dest_dir = os.path.join(work_home, str(now.year), str(now.month))

        return dest_dir

    def get_store_path(self, filename):
        if not filename:
            raise ValueError('Must specify filename parameter')

        dest_dir = self.get_store_dir()
        dest_path = os.path.join(dest_dir, filename)

        if not os.path.isdir(dest_dir):
            os.makedirs(dest_dir)
            return dest_path

        if os.path.isfile(dest_path):
            ind = dest_path.rfind('.')
            if ind != -1:
                prefix = dest_path[:ind]
                suffix = dest_path[ind:]
            else:
                prefix = dest_path
                suffix = ''

            ind2 = prefix.rfind('_')
            if ind2 == -1:
                dest_path = '{}_1{}'.format(prefix, suffix)
            else:
                last_num_str = prefix[ind2+1:]
                if last_num_str:
                    try:
                        last_num = int(last_num_str)
                    except ValueError:
                        # file name ends with '_xx' but 'xx' is not a number
                        dest_path = '{}_1{}'.format(prefix, suffix)
                    else:
                        # file name ends with '_xx' and 'xx' is not a number
                        dest_path = '{}_{}{}'.format(prefix[:ind2], last_num + 1, suffix)
                else:
                    # file name ends with '_'
                    dest_path = '{}_1{}'.format(prefix, suffix)

        return dest_path
