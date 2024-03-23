#!/usr/bin/python3
""" Test """
from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class test_state(TestBasemodel):
    """ Test """

    def __init__(self, *args, **kwargs):
        """ Test """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test """
        new = self.value()
        self.assertEqual(type(new.name), str)
