#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
import models


class TestDBStorage(unittest.TestCase):
    """ Test """
    @unittest.skipIf(not models.is_db, "DB storage")
    def test_all_returns_dict(self):
        """ Test """

    @unittest.skipIf(not models.is_db, "DB storage")
    def test_new(self):
        """ Test """

    @unittest.skipIf(not models.is_db, "DB storage")
    def test_reload(self):
        """ Test """

    @unittest.skipIf(not models.is_db, "DB storage")
    def test_save(self):
        """ Test """
