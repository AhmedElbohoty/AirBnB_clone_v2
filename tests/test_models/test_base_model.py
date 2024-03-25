#!/usr/bin/python3
""" Test """
import os
import unittest
import datetime
import json
import models
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_default(self):
        """ Test """
        i = self.value()
        self.assertEqual(type(i), self.value)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_kwargs(self):
        """ Test """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_kwargs_int(self):
        """ Test """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_str(self):
        """ Test """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_todict(self):
        """ Test """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_kwargs_none(self):
        """ Test """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_id(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_created_at(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skipIf(models.is_db, "Test for Files Storage")
    def test_updated_at(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
