import unittest

from leap import leap


class TestLeap(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leap(1900), False)
        self.assertEqual(leap(1997), False)
        self.assertEqual(leap(2000), True)
        self.assertEqual(leap(2016), True)
        self.assertEqual(leap(2015), False)
        self.assertEqual(leap(2100), False)
        self.assertEqual(leap(2000), True)
