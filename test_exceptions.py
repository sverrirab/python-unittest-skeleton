import unittest


class TestSuccess(unittest.TestCase):

    def test_failure(self):
        with self.assertRaises(ZeroDivisionError):
            invalid = 1 / 0
