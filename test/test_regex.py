"""
https://www.hackerrank.com/domains/regex
"""

import re


def test_uk_telephone_num():
    regex = '^\d{11}$'
    assert re.search(regex, '12345678901') is not None
    assert re.search(regex, '6101234567') is None


def test_caputure_group():
    """
    'ok' 3 or more times
    """
    regex = '(ok){3,}'
    assert re.search(regex, 'okokok! cya') is not None


def test_range():
    """
    string length >= 5
    1 - lowercase letter
    2 - positive num
    3 - not a lowercase letter
    4 - not a uppercase letter
    5 - uppercase letter
    """
    regex = '^[a-z][1-9][^a-z][^A-Z][A-Z]'
    assert re.search(regex, 'h4CkR') is not None


def test_exclude_specific_char():
    """
    1 - no digits
    2 - no lowercase vowels
    3 - not b, c, D, F
    4 - no whitespace char
    5 - no uppercase vowels
    6 - neither . nor ,
    """
    regex = '^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.\,]$'
    assert re.search(regex, 'think?') is not None


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
