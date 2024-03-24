#!/usr/bin/python3
""" Test """
import unittest
import models
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_city_id(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_user_id(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_name(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_description(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_number_rooms(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_number_bathrooms(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_max_guest(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_price_by_night(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_latitude(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_longitude(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_amenity_ids(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
