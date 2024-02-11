#!/usr/bin/python3

import unittest

from models.city import City


class TestCityModel(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_init(self):
        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_str(self):
        self.assertIn("City", str(self.city))
        self.assertIn("id", str(self.city))
        self.assertIn("created_at", str(self.city))
        self.assertIn("updated_at", str(self.city))
        self.assertIn("state_id", str(self.city))
        self.assertIn("name", str(self.city))

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)


if __name__ == '__main__':
    unittest.main()
