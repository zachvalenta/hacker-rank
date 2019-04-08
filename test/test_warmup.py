from src.warmup import counting_valleys, jump_clouds, repeated_string, sock_merchant


def test_counting_valleys():
    """
    _/\_______
       \    /
        \/\/
    """
    assert counting_valleys(s="UDDDUDUU") == 1
    """
    __________
    \/\      /
       \  /\/
        \/
    """
    assert counting_valleys(s="DDUUDDUDUUUD") == 2
    """
         /\/\
        /    \
    _/\/______\
    """
    assert counting_valleys(s="UDUUUDUDDD") == 0
    """
    __________________
    \/\      /
       \  /\/
        \/
    """
    assert counting_valleys(s="DUDDDUUDUU") == 2


def test_jump_clouds():
    assert jump_clouds([0, 0, 0, 1, 0, 0]) == 3
    assert jump_clouds([0, 1, 0, 0, 0, 1, 0]) == 3
    assert jump_clouds([0, 0, 1, 0, 0, 1, 0]) == 4


def test_repeat_string():
    assert repeated_string(s="aba", n=10) == 7
    assert repeated_string(s="a", n=1000000000000) == 1000000000000
    assert repeated_string(s="aab", n=882787) == 588525


def test_sock_merchant():
    assert sock_merchant(ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
