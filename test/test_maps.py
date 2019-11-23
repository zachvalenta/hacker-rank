from src.maps import common_substring


def test_common_substring():
    assert common_substring("hello", "world") == "YES"
    assert common_substring("hi", "world") == "NO"
