import unittest

from localspelling.spelling_converter import convert_spelling


class TestAggItemCounts(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual("the", convert_spelling("the", "gb"))

    def test_single_word_gb_to_us(self):
        self.assertEqual("honor", convert_spelling("honour", "us"))

    def test_single_word_us_to_gb(self):
        self.assertEqual("honour", convert_spelling("honor", "gb"))

    def test_single_word_us_to_gb_unchanged_because_already_in_target_locale(self):
        self.assertEqual("honour", convert_spelling("honour", "gb"))

    def test_single_word_case_conserved(self):
        self.assertEqual("it is of a good Caliber blah blah center potato",
                         convert_spelling("it is of a good Calibre blah blah centre potato", "us"))

    def test_single_word_case_conserved_all_caps(self):
        self.assertEqual("i was MANEUVERING down the road", convert_spelling("i was MANOEUVRING down the road", "us"))

    def test_converting_short_word(self):
        self.assertEqual("an eon", convert_spelling("an aeon", "us"))

    def test_not_converting_substring(self):
        self.assertEqual("a xaeon", convert_spelling("a xaeon", "us"))

    def test_converting_labor_without_suffix(self):
        self.assertEqual("it was labour ", convert_spelling("it was labor ", "gb"))

    def test_not_doing_laborious_with_suffix(self):
        self.assertEqual("it was laborious ", convert_spelling("it was laborious ", "gb"))

    def test_nonexistent_suffix(self):
        self.assertEqual("potatoficisation sdfsdf", convert_spelling("potatoficization sdfsdf", "gb"))
