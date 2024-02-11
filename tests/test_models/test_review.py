#!/usr/bin/python3

import unittest

from models.review import Review


class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review

    def test_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_str(self):
        string_repr = str(self.review)
        self.assertIn("[Review]", string_repr)
        self.assertIn("id", string_repr)
        self.assertIn("created_at", string_repr)
        self.assertIn("updated_at", string_repr)
        self.assertIn("place_id", string_repr)
        self.assertIn("user_id", string_repr)
        self.assertIn("text", string_repr)

    def test_save(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict(self):
        rev_dict = self.review.to_dict()
        self.assertIsInstance(rev_dict, dict)
        self.assertEqual(rev_dict['__class__'], 'Review')
        self.assertEqual(rev_dict['place_id'], self.review.place_id)
        self.assertEqual(rev_dict['text'], self.review.text)
        self.assertIn('id', rev_dict)
        self.assertIn('created_at', rev_dict)
        self.assertIn('updated_at', rev_dict)
        self.assertIn('place_id', rev_dict)
        self.assertIn('user_id', rev_dict)
        self.assertIn('text', rev_dict)


if __name__ == '__main__':
    unittest.main()
