import random
import unittest

ARRAY = [False, True, True, True, True]
random.shuffle(ARRAY)


class TestFlaky(unittest.TestCase):

    def test_1_flaky(self):
        self.assertTrue(ARRAY[0], "Flaky candidate number 1")

    def test_2_flaky(self):
        self.assertTrue(ARRAY[1], "Flaky candidate number 2")

    def test_3_flaky(self):
        self.assertTrue(ARRAY[2], "Flaky candidate number 3")

    def test_4_flaky(self):
        self.assertTrue(ARRAY[3], "Flaky candidate number 4")

    def test_5_flaky(self):
        self.assertTrue(ARRAY[4], "Flaky candidate number 5")

