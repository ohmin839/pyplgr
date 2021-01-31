import unittest
from parameterized import parameterized
from pyplgr.plgrcoll.api import without_iota_subscriptum

class WithoutIotaSubscriptumTest(unittest.TestCase):
    @parameterized.expand([
        ["ᾳ", "α"],
        ["ᾴ", "ά"],
        ["ᾲ", "ὰ"],
        ["ᾷ", "ᾶ"],
        ["ᾁ", "ἁ"],
        ["ᾅ", "ἅ"],
        ["ᾃ", "ἃ"],
        ["ᾇ", "ἇ"],
        ["ᾀ", "ἀ"],
        ["ᾄ", "ἄ"],
        ["ᾂ", "ἂ"],
        ["ᾆ", "ἆ"],
        ["ῃ", "η"],
        ["ῄ", "ή"],
        ["ῂ", "ὴ"],
        ["ῇ", "ῆ"],
        ["ᾑ", "ἡ"],
        ["ᾕ", "ἥ"],
        ["ᾓ", "ἣ"],
        ["ᾗ", "ἧ"],
        ["ᾐ", "ἠ"],
        ["ᾔ", "ἤ"],
        ["ᾒ", "ἢ"],
        ["ᾖ", "ἦ"],
        ["ῳ", "ω"],
        ["ῴ", "ώ"],
        ["ῲ", "ὼ"],
        ["ῷ", "ῶ"],
        ["ᾡ", "ὡ"],
        ["ᾥ", "ὥ"],
        ["ᾣ", "ὣ"],
        ["ᾧ", "ὧ"],
        ["ᾠ", "ὠ"],
        ["ᾤ", "ὤ"],
        ["ᾢ", "ὢ"],
        ["ᾦ", "ὦ"],
        ["ᾼ", "Α"],
        ["Ὰ", "Ά"],
        ["ᾉ", "Ἁ"],
        ["ᾍ", "Ἅ"],
        ["ᾋ", "Ἃ"],
        ["ᾏ", "Ἇ"],
        ["ᾈ", "Ἀ"],
        ["ᾌ", "Ἄ"],
        ["ᾊ", "Ἂ"],
        ["ᾎ", "Ἆ"],
        ["ῌ", "Η"],
        ["Ὴ", "Ή"],
        ["ᾙ", "Ἡ"],
        ["ᾝ", "Ἥ"],
        ["ᾛ", "Ἣ"],
        ["ᾟ", "Ἧ"],
        ["ᾘ", "Ἠ"],
        ["ᾜ", "Ἤ"],
        ["ᾚ", "Ἢ"],
        ["ᾞ", "Ἦ"],
        ["ῼ", "Ω"],
        ["Ὼ", "Ώ"],
        ["ᾩ", "Ὡ"],
        ["ᾭ", "Ὥ"],
        ["ᾫ", "Ὣ"],
        ["ᾯ", "Ὧ"],
        ["ᾨ", "Ὠ"],
        ["ᾬ", "Ὤ"],
        ["ᾪ", "Ὢ"],
        ["ᾮ", "Ὦ"],
        ["0", "0"],
    ])
    def test_without_iota_subscriptum(self, text, expected):
        actual = without_iota_subscriptum(text)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
