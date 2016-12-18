#!/usr/bin/evn python
# -*- coding: utf-8 -*-

__author__ = 'weichen2046@gmail.com'


import os
import unittest

from storage import StorageManager


class StorageTester(unittest.TestCase):

    def test_get_store_path(self):
        sm = StorageManager()
        store_dir = sm.get_store_dir()

        # file not exist
        # file with suffix
        filename = 'chenwei.txt'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        filename = 'chenwei_.txt'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        filename = 'chenwei_1.txt'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        filename = 'chenwei_a.txt'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        # file not with suffix
        filename = 'chenwei'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        filename = 'chenwei_'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        filename = 'chenwei_1'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        filename = 'chenwei_a'
        self.assertEqual(os.path.join(store_dir, filename), sm.get_store_path(filename))

        # file exist
        # file with suffix
        filename = 'chenwei.txt'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei_1.txt'), sm.get_store_path(filename))
        os.remove(tmpfile)

        filename = 'chenwei_.txt'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei__1.txt'), sm.get_store_path(filename))
        os.remove(tmpfile)

        filename = 'chenwei_1.txt'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei_2.txt'), sm.get_store_path(filename))
        os.remove(tmpfile)

        filename = 'chenwei_a.txt'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei_a_1.txt'), sm.get_store_path(filename))
        os.remove(tmpfile)

        # file not with suffix
        filename = 'chenwei'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei_1'), sm.get_store_path(filename))
        os.remove(tmpfile)

        filename = 'chenwei_'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei__1'), sm.get_store_path(filename))
        os.remove(tmpfile)

        filename = 'chenwei_1'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei_2'), sm.get_store_path(filename))
        os.remove(tmpfile)

        filename = 'chenwei_a'
        tmpfile = sm.get_store_path(filename)
        open(tmpfile, 'a').close()
        self.assertEqual(os.path.join(store_dir, 'chenwei_a_1'), sm.get_store_path(filename))
        os.remove(tmpfile)


if __name__ == '__main__':

    unittest.main()
