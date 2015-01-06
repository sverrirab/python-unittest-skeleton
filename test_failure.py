import unittest


class TestFailure(unittest.TestCase):

    def test_1_ok(self):
        self.assertTrue(True)

    def test_2_failing(self):
        self.assertTrue(False, "I know, this should always fail")

    @unittest.skip("This test is intentionally skipped")
    def test_3_skip(self):
        self.assertTrue(False)

    def test_4_ok(self):
        self.assertTrue(True)
