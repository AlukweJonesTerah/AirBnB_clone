#!/usr/bin/python3

"""
Unittest for BaseModel class
"""

import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_string(self):
        self.assertIn("BaseModel", str(self.base_model))
        self.assertIn("id", str(self.base_model))
        self.assertIn("created_at", str(self.base_model))
        self.assertIn("updated_at", str(self.base_model))

    def test_save(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


if __name__ == '__main__':
    unittest.main()
