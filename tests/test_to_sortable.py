import unittest
from parameterized import parameterized
from pyplgr.plgrcoll.api import to_sortable

class ToSortableTest(unittest.TestCase):
    @parameterized.expand([
        ["Πάντες", "παντες"],
        ["Σωκράτει", "σωκρατει"],
        ["Ἐπεὶ", "επει"],
        ["Ὅτι", "οτι"],
        ["Πρῶτον", "πρωτον"],
        ["ὑποκειμένῳ", "υποκειμενω"],
    ])
    def test_to_sortable(self, text, expected):
        actual = to_sortable(text)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
