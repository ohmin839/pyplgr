import unittest
from parameterized import parameterized
from pyplgr.collector.api import to_words_list

class ToWordsList(unittest.TestCase):
    @parameterized.expand([
        ["", []],
        ["α", ["α"]],
        ["δ'", ["δ'"]],
        ["ὁ ἄνθρώπός τις", ["ὁ", "ἄνθρώπός", "τις"]],
    ])
    def test_to_words_list(self, text, expected):
        actual = to_words_list(text)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
