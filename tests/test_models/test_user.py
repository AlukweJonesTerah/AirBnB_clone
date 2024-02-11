#!/usr/bin/python3

import unittest

from models.user import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_init(self):
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_str(self):
        self.assertIn("[User]", str(self.user))
        self.assertIn("id", str(self.user))
        self.assertIn("created_at", str(self.user))
        self.assertIn("updated_at", str(self.user))
        self.assertIn("email", str(self.user))
        self.assertIn("password", str(self.user))
        self.assertIn("first_name", str(self.user))
        self.assertIn("last_name", str(self.user))

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)


if __name__ == '__main__':
    unittest.main()
