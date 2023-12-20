#!/usr/bin/python3
"""Module with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os


class test_state(test_basemodel):
    """Class with tests"""

    @classmethod
    def setUpClass(cls):
        """Setting up"""
        cls.state = State()
        cls.state.name = "SomeState"

    @classmethod
    def teardown(cls):
        """Tearing down"""
        del cls.state

    def __init__(self, *args, **kwargs):
        """Initializing"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_name3(self):
        """Testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_attributes_state(self):
        """Testing attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attribute_types_state(self):
        """Testing types"""
        self.assertEqual(type(self.state.name), str)

    def test_save_state(self):
        """Testing save"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_state(self):
        """Testing dict"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
