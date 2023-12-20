#!/usr/bin/python3
"""Module with a class with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import pep8


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "WiFi"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes_amenity(self):
        """Testing attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_types_amenity(self):
        """Testing attribute types"""
        self.assertEqual(type(self.amenity.name), str)


if __name__ == "__main__":
    unittest.main()
