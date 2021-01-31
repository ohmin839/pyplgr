import unittest
from parameterized import parameterized
from pyplgr.plgrcoll.api import without_dialesis

class WithoutDialesisTest(unittest.TestCase):
    @parameterized.expand([
        ["ϊ", "ι"],
        ["ΐ", "ί"],
        ["ῒ", "ὶ"],
        ["ῗ", "ῖ"],
        ["ϋ", "υ"],
        ["ΰ", "ύ"],
        ["ῢ", "ὺ"],
        ["ῧ", "ῦ"],
        ["0", "0"],
    ])
    def test_without_accent(self, text, expected):
        actual = without_dialesis(text)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
