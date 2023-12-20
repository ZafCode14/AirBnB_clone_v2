#!/usr/bin/python3
"""Module with unittest"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os
import pep8


class test_review(test_basemodel):
    """Class with tests"""

    @classmethod
    def setUpClass(cls):
        """Setting up"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """Tearing down"""
        del cls.rev

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def __init__(self, *args, **kwargs):
        """Initializing"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_place_id(self):
        """Testing place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_user_id(self):
        """Testing user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', 'Not file engine')
    def test_text(self):
        """Testing text"""
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_attributes_review(self):
        """Testing attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_attribute_types_review(self):
        """Testing types of attr"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)


if __name__ == "__main__":
    unittest.main()
