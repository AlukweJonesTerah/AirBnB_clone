#!/usr/bin/python3

import unittest

from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_str(self):
        self.assertIn("Amenity", str(self.amenity))
        self.assertIn("id", str(self.amenity))
        self.assertIn("created_at", str(self.amenity))
        self.assertIn("updated_at", str(self.amenity))
        self.assertIn("name", str(self.amenity))

    def test_save(self):
        old_created_at = self.amenity.created_at
        self.amenity.save()
        self.assertNotEqual(old_created_at, self.amenity.created_at)

    def test_to_dict(self):
        am_dict = self.amenity.to_dict()
        self.assertIsInstance(am_dict, dict)
        self.assertEqual(am_dict["__class__"], "Amenity")
        self.assertIn("id", am_dict)
        self.assertIn('created_at', am_dict)
        self.assertIn('updated_at', am_dict)
        self.assertIn('name', am_dict)


if __name__ == "__main__":
    unittest.main()
