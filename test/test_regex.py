"""
https://www.hackerrank.com/domains/regex
"""

import re


def test_digits_and_non_digits():
    """
    anything in the format ddDddDdddd
    """
    regex = '\d\d\D\d\d\D\d\d\d\d'
    assert re.match(regex, '06-11-2015') is not None


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
