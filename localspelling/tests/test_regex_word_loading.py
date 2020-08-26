import unittest

from localspelling.util import get_regex_and_raw_word


class TestAggItemCounts(unittest.TestCase):

    def test_no_change_regex(self):
        self.assertEqual(r'\bthe\b', get_regex_and_raw_word("the")[0])

    def test_no_change_word(self):
        self.assertEqual("the", get_regex_and_raw_word("the")[1])

    def test_prefix_regex(self):
        self.assertEqual(r'the\b', get_regex_and_raw_word("*the")[0])

    def test_prefix_word(self):
        self.assertEqual("the", get_regex_and_raw_word("*the")[1])

    def test_suffix_regex(self):
        self.assertEqual(r'\bthe', get_regex_and_raw_word("the*")[0])

    def test_suffix_word(self):
        self.assertEqual("the", get_regex_and_raw_word("the*")[1])

    def test_prefix_suffix_regex(self):
        self.assertEqual(r'the', get_regex_and_raw_word("*the*")[0])

    def test_prefix_suffix_word(self):
        self.assertEqual("the", get_regex_and_raw_word("*the*")[1])
