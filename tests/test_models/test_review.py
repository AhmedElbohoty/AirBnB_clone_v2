#!/usr/bin/python3
""" Test """
import unittest
import models
from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_place_id(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_user_id(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_text(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.text), str)
