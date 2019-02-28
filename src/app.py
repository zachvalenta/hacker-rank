"""
https://www.hackerrank.com/interview/interview-preparation-kit/warmup/challenges
"""


def sock_merchant(n, ar):
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
