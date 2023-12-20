#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
