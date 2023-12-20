#!/usr/bin/python3
"""Module with unittest"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Class with tests"""
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """Tests the create command with the file storage.  """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User name="Mike" age=23 height=2.1')
            output = f.getvalue().strip()
            self.assertIn("User.{}".format(output), storage.all().keys())
            user_id = "User.{}".format(output)
            created_user = storage.all()[user_id]
            self.assertEqual(created_user.name, "Mike")
            self.assertEqual(created_user.age, 23)
            self.assertEqual(created_user.height, 2.1)
