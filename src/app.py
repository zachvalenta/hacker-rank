"""
https://www.hackerrank.com/interview/interview-preparation-kit/warmup/challenges
"""


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
            pairs.update({el: pairs[el]+1})
        if pairs[el] == 2:
            tally += 1
            pairs.update({el: 0})
    return tally


def counting_valleys(s):
    """
    scratch the phrase 'consecutive steps' from the problem statement
    you only care if you go below sea level and come back up again
    """
    sea_level = 0
    valleys = 0
    for i, v in list(enumerate(s)):
        current_sea_level = sea_level
        if v == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        if current_sea_level == 0 and sea_level < 0:
            valleys += 1
    return valleys
