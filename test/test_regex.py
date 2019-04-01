"""
https://www.hackerrank.com/domains/regex
"""

import re


def test_match_specific_char():
    """
    this prompt is too inane to bother enumerating
    """
    regex = '^[1-3][0-2][x|s|0][a|A|0|3][x|s|u][\.|,]$'
    assert re.search(regex, '1203x.') is not None


def test_matching_start_end():
    """
    anything in the format Dwwwww.
    """
    regex = '^\d\w{4}\.$'
    assert re.search(regex, '0qwer.') is not None


def test_word_and_non_word():
    """
    anything in the format xxxXxxxxxxxxxxXxxx
    """
    regex = '\w{3}\W\w{10}\W\w{3}'
    assert re.search(regex, 'www.hackerrank.com') is not None


def test_whitespace_and_non_whitespace():
    pass
    """
    anything in the format XXxXXxXX
    """
    regex = '\S{2}\s\S{2}\s\S{2}'
    assert re.search(regex, '12 11 15') is not None


def test_digits_and_non_digits():
    """
    anything in the format ddDddDdddd
    """
    regex = '\d{2}\D\d{2}\D\d{4}'
    assert re.search(regex, '06-11-2015') is not None


def test_any_but_newline():

    """
    3char.3char.3char.3char --> i.e. exactly 4x
    only constraint on char is that it's not a new line
    """

    regex = '(.{3}\.){3}(.{3})$'
    assert re.match(regex, '123.456.abc.def') is not None
    assert re.match(regex, '...............') is not None
    assert re.match(regex, '1123.456.abc.def') is None
    assert re.match(regex, '123.123.123.132.123.123') is None
