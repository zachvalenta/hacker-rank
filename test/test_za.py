from src.za import container_ship, find_longest_substring, word_count


def test_container_ship():
    consumption = [3, 5, 2, 1]
    timestamps = [0, 3, 5, 8]
    assert container_ship(cons=consumption, stamps=timestamps) == 25


def test_find_longest_substring():
    assert find_longest_substring('') == 0
    assert find_longest_substring('bbbb') == 1
    assert find_longest_substring('abcabcbb') == 3
    assert find_longest_substring('pwwkew') == 3


def test_word_count():
    most_common = [('of', 12), ('the', 10), ('his', 10), ('and', 9), ('to', 8)]
    assert word_count(version='ordered')[:5] == most_common
    assert word_count(version='scrambled')[:5] == most_common
    assert word_count(version='missing-final-the')[:5] != most_common
