from unittest import TestCase

from keyutil import keyutil


class TestKeyutil(TestCase):

    def test_get_random_string_type(self):
        s = keyutil.get_random_string()
        self.assertIsNotNone(s, 'should not be None')
        self.assertTrue(isinstance(s, str), 'should be str')

    def test_get_random_string_length(self):
        s = keyutil.get_random_string(length=12)
        self.assertTrue(len(s) == 12, 'incorrect length')
        self.assertFalse(len(s) < 12, 'incorrect length')
        self.assertFalse(len(s) > 12, 'incorrect length')

    def test_get_random_string_chars(self):
        good_chars = 'abcXYZ'
        bad_chars = '!@#$%^&*()'
        s = keyutil.get_random_string(allowed_chars='abcXYZ')

        self.assertTrue(any([ch in s for ch in good_chars]),
                'at least one of these chars must be in the string')

        self.assertFalse(all([ch in s for ch in bad_chars]),
                'none of these chars can be in the string')
