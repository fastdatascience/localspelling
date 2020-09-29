import unittest

from localspelling.spelling_converter import get_dictionary


class TestSingleWord(unittest.TestCase):

    def test_us(self):
        self.assertEqual("honor", get_dictionary("us")["honour"])

    def test_gb(self):
        self.assertEqual("honour", get_dictionary("gb")["honor"])
