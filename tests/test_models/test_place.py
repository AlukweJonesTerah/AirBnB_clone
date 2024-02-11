#!/usr/bin/python3

import unittest

from models.place import Place


class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_init(self):
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_str(self):
        self.assertIn("[Place]", str(self.place))
        self.assertIn("id", str(self.place))
        self.assertIn("created_at", str(self.place))
        self.assertIn("updated_at", str(self.place))
        self.assertIn("city_id", str(self.place))
        self.assertIn("user_id", str(self.place))
        self.assertIn("name", str(self.place))
        self.assertIn("description", str(self.place))
        self.assertIn("number_rooms", str(self.place))
        self.assertIn("number_bathrooms", str(self.place))
        self.assertIn("max_guest", str(self.place))
        self.assertIn("price_by_night", str(self.place))
        self.assertIn("latitude", str(self.place))
        self.assertIn("longitude", str(self.place))
        self.assertIn("amenity_ids", str(self.place))

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_save(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)


if __name__ == '__main__':
    unittest.main()
