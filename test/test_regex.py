"""
https://www.hackerrank.com/domains/regex
"""

import re


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
