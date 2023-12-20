#!/usr/bin/python3
"""Module with a unittest"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8


class test_basemodel(unittest.TestCase):
    """Clase with tests"""

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/base_model.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def __init__(self, *args, **kwargs):
        """Initializing"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        """Testing default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Testing kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Testign kwargs int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Testign string"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Testign to dict"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Testign none kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not db engine')
    def test_kwargs_one(self):
        """Testign if one kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Testing id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Testing created at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Testing updated at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)


if __name__ == "__main__":
    unittest.main()
