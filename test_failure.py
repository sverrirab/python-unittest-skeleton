import unittest


class TestFailure(unittest.TestCase):

    def test_1_ok(self):
        self.assertTrue(True)

    def test_2_failing(self):
        self.assertTrue(False, "I know, this should always fail")

    def test_3_ok(self):
        self.assertTrue(True)