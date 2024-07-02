import pytest
from pyplgrapi import to_words_list

@pytest.mark.parametrize(
    [
        "text",
        "expected"
    ],
    [
        pytest.param("", []),
        pytest.param("α", ["α"]),
        pytest.param("δ'", ["δ'"]),
        pytest.param("ὁ ἄνθρώπός τις", ["ὁ", "ἄνθρώπός", "τις"]),
    ]
)
def test_to_words_list(text, expected):
    actual = to_words_list(text)
    assert expected == actual
