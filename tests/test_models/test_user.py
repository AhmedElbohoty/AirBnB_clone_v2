#!/usr/bin/python3
""" Test """
import unittest
import models
from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class TestUser(TestBasemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_first_name(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_last_name(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_email(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_password(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.password), str)
