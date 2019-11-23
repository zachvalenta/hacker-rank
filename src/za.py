from collections import Counter
import json
from os import path


def container_ship(cons, stamps):
    """
    consumption = [3, 5, 2, 1]
    timestamps = [0, 3, 5, 8]

    0 to 3 = 3 hours * 3 = 9 tons consumed
    3 to 5 = 2 hours * 6 = 10 tons consumed
    5 to 8 = 3 hours * 2 = 6 tons consumed

    25 tons total
    """
    total_cost = 0
    for x, y in zip(cons, stamps):
        next_i = stamps.index(y) + 1
        if next_i <= len(stamps) - 1:
            next_val = stamps[next_i]
            elapsed_time = next_val - y
            current_cost = elapsed_time * x
            total_cost += current_cost
    return total_cost


def find_longest_substring(query):
    """
    find length of longest substring w/out repeating char

    further cases ⬇️

    assert scaffold('a') == 1
    assert scaffold('abcdbefghi') == ?
    """
    current = ""
    longest = 0
    for i, v in enumerate(query):
        if i == 0:
            longest = len(current)
            current += v
        else:
            if v in current and len(current) > longest:
                longest = len(current)
                current = v
            elif v in current:
                current = ""
            else:
                current += v
    return longest


def word_count(version, output=False):
    basepath = path.dirname(__file__)
    austen = path.abspath(path.join(basepath, "..", "austen.json"))
    with open(austen) as f:
        text = json.load(f)["austen-{}".format(version)]
        ranked = Counter(text.split()).most_common()
        if output:
            print(*ranked, sep="\n")
        else:
            return ranked
