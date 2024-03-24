#!/usr/bin/python3
""" Test """
import unittest
import models
from tests.test_models.test_base_model import TestBasemodel
from models.city import City


class TestCity(TestBasemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_state_id(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_name(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.name), str)
