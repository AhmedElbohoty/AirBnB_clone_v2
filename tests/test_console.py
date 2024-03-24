#!/usr/bin/python3
'''Unit tests for base model module'''
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    '''Unit tests for hbnb command'''

    def test_create_user(self):
        '''Tests for create method'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User age=25")

            obj_id = f.getvalue().strip()
            self.assertTrue(type(obj_id) is str)
