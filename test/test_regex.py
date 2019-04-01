"""
https://www.hackerrank.com/domains/regex
"""

import re


def test_whitespace_and_non_whitespace():
    pass
    """
    anything in the format XXxXXxXX
    """
    regex = '\S\S\s\S\S\s\S\S'
    assert re.search(regex, '12 11 15') is not None


def test_digits_and_non_digits():
    """
    anything in the format ddDddDdddd
    """
    regex = '\d\d\D\d\d\D\d\d\d\d'
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
