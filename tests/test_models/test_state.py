#!/usr/bin/python3

import unittest

from models.state import State


class TestStateModel(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_instance_creation(self):
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_str(self):
        self.assertIn("[State]", str(self.state))
        self.assertIn("id", str(self.state))
        self.assertIn("created_at", str(self.state))
        self.assertIn("updated_at", str(self.state))
        self.assertIn("name", str(self.state))

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], self.state.name)
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)


if __name__ == '__main__':
    unittest.main()
