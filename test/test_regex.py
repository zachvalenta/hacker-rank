"""
https://www.hackerrank.com/domains/regex
"""

import re


def test_word_boundary():
    """
    - starts w/ lower/upper vowel
    - full match only letters
    - full match can be any length
    - must start and end w/ word boundary
    """
    regex = r"\b[aeiouAEIOU][a-zA-Z]*\b"
    assert re.search(regex, "Found any match?") is not None


def test_ending_items():
    """
    - consist of only lower/uppercase
    - end in 's'
    """
    regex = "^[a-zA-Z]*s$"
    assert re.search(regex, "Kites") is not None
    assert re.search(regex, "s") is not None
    assert re.search(regex, "3ess") is None


def test_match_repetitions_one_or_more():
    """
    - begin w/ 1 or more digits
    - followed by 1 or more uppercase letters
    - end w/ 1 or more lowercase letters
    """
    regex = "^\d+[A-Z]+[a-z]+$"
    assert re.search(regex, "1Qa") is not None


def test_match_repetitions_zero_or_more():
    """
    - begin w/ 2 or more digits
    - followed by 0 or more lowercase letters
    - end w/ 0 or more lowercase letters
    """
    regex = "^\d{2,}[a-z]*[A-Z]*$"
    assert re.search(regex, "14") is not None


def test_match_repetitions_specific():
    """
    - begin w/ 1 or 2 digits
    - followed by 3 or more letters
    - end w/ up to 3 '.'
    """
    regex = "^\d{1,2}[a-zA-Z]{3,}\.{0,3}$"
    assert re.search(regex, "3threeormorealphabets.") is not None
    assert re.search(regex, "3threeormorealphabets....") is None


def test_match_repetitions():
    """
    first 40 - any alphabetic or even num
    last 5 - odd digits or whitespace char
    """
    regex = "^[a-zA-Z|02468]{40}([13579|\s]{5})$"
    assert re.search(regex, "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57") is not None
    assert re.search(regex, "x4202v2A22A9a6aaaaaa2G2222m222qwertyYuIo13957") is None


def test_honorific():
    regex = "^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$"
    assert re.search(regex, "Mr.DOSHI") is not None
    assert re.search(regex, "Mr.V.K. Doshi") is None
    assert re.search(regex, "Ms._underscore") is None


def test_email():
    """
    - any alphanumeric, hyphen, dot
    @
    - any alphanumeric, hyphen
    .
    - any alphabetic
    """
    regex = "^([\w\.-]+)@([\w-]+)\.([a-zA-Z]+)$"
    assert re.search(regex, "zjv1000@yahoo.com") is not None
    assert re.search(regex, "zjv.1000@yahoo.com") is not None
    assert re.search(regex, "zjv-1000@yahoo.com") is not None
    assert re.search(regex, "zjv1000@yahoo.org") is not None
    assert re.search(regex, "zjv1000#yahoo.com") is None
    assert re.search(regex, "zjv1000@yahoo.123") is None


def test_uk_telephone_num():
    regex = "^\d{11}$"
    assert re.search(regex, "12345678901") is not None
    assert re.search(regex, "6101234567") is None


def test_caputure_group():
    """
    'ok' 3 or more times
    """
    regex = "(ok){3,}"
    assert re.search(regex, "okokok! cya") is not None


def test_range():
    """
    string length >= 5
    1 - lowercase letter
    2 - positive num
    3 - not a lowercase letter
    4 - not a uppercase letter
    5 - uppercase letter
    """
    regex = "^[a-z][1-9][^a-z][^A-Z][A-Z]"
    assert re.search(regex, "h4CkR") is not None


def test_exclude_specific_char():
    """
    1 - no digits
    2 - no lowercase vowels
    3 - not b, c, D, F
    4 - no whitespace char
    5 - no uppercase vowels
    6 - neither . nor ,
    """
    regex = "^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.\,]$"
    assert re.search(regex, "think?") is not None


def test_match_specific_char():
    """
    this prompt is too inane to bother enumerating
    """
    regex = "^[1-3][0-2][x|s|0][a|A|0|3][x|s|u][\.|,]$"
    assert re.search(regex, "1203x.") is not None


def test_matching_start_end():
    """
    anything in the format Dwwwww.
    """
    regex = "^\d\w{4}\.$"
    assert re.search(regex, "0qwer.") is not None


def test_word_and_non_word():
    """
    anything in the format xxxXxxxxxxxxxxXxxx
    """
    regex = "\w{3}\W\w{10}\W\w{3}"
    assert re.search(regex, "www.hackerrank.com") is not None


def test_whitespace_and_non_whitespace():
    pass
    """
    anything in the format XXxXXxXX
    """
    regex = "\S{2}\s\S{2}\s\S{2}"
    assert re.search(regex, "12 11 15") is not None


def test_digits_and_non_digits():
    """
    anything in the format ddDddDdddd
    """
    regex = "\d{2}\D\d{2}\D\d{4}"
    assert re.search(regex, "06-11-2015") is not None


def test_any_but_newline():

    """
    3char.3char.3char.3char --> i.e. exactly 4x
    only constraint on char is that it's not a new line
    """

    regex = "(.{3}\.){3}(.{3})$"
    assert re.match(regex, "123.456.abc.def") is not None
    assert re.match(regex, "...............") is not None
    assert re.match(regex, "1123.456.abc.def") is None
    assert re.match(regex, "123.123.123.132.123.123") is None
