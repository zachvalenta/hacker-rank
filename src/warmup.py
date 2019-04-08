"""
https://www.hackerrank.com/interview/interview-preparation-kit/warmup/challenges
"""


def counting_valleys(s):
    """
    * count number of time you go below and then return to sea level
    * scratch the phrase 'consecutive steps' from the problem statement
    """
    sea_level = 0
    valleys = 0
    for i, v in list(enumerate(s)):
        current_sea_level = sea_level
        if v == "U":
            sea_level += 1
        else:
            sea_level -= 1
        if current_sea_level == 0 and sea_level < 0:
            valleys += 1
    return valleys


def jump_clouds(c):
    """
    * input is list of 0s and 1s
    * get to last index in as few moves as possible
    * can move to index that is is either 1 or 2 greater than current
     index i.e. at index 2, can move to indices 3 or 4
    * cannot move to index where value is 1
    """

    jumps = 0
    pairs = [x for x in enumerate(c)]
    index = 0
    index_end = len(c) - 1

    while index != index_end:
        if pairs[index + 1][0] == index_end:
            jumps += 1
            break
        if pairs[index + 2][1] != 1:
            jumps += 1
            index += 2
        else:
            jumps += 1
            index += 1
    return jumps


def repeated_string(s, n):
    whole = n // len(s)
    remainder = n % len(s)
    base_count = whole * s.count("a")
    return base_count + s[:remainder].count("a")


def sock_merchant(ar):
    """
    sample input:
    n - 9
    ar - 10, 20, 20, 10, 10, 30, 50, 10, 20

    sample output:
    3
    """
    pairs = dict()
    tally = 0
    for el in ar:
        if el not in pairs:
            pairs[el] = 1
        else:
            pairs.update({el: pairs[el] + 1})
        if pairs[el] == 2:
            tally += 1
            pairs.update({el: 0})
    return tally
