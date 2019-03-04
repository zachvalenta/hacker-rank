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
    toggle = False
    counter = 0
    for i, v in list(enumerate(s)):
        if i == len(s)-1:
            return counter
        if v == s[i+1] and toggle is False and v == 'D':
            toggle = True
        if v != s[i + 1] and toggle is True:
            counter += 1
        if v != s[i + 1]:
            toggle = False
