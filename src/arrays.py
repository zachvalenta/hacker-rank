"""
https://www.hackerrank.com/interview/interview-preparation-kit/arrays/challenges
"""


def sum_hourglass(arr):
    global_high = 0
    for ind, two_d in list(enumerate(arr))[:4]:
        for sy, el in list(enumerate(two_d))[:4]:
            local_high = 0
            top_sum = sum(two_d[sy : sy + 3])
            mid_sum = arr[ind + 1][sy + 1]
            btm_sum = sum(arr[ind + 2][sy : sy + 3])
            local_high += top_sum + mid_sum + btm_sum
            if (
                ind == 0 and sy == 0
            ) or local_high >= global_high:  # solves if all sums negative
                global_high = local_high
    return global_high
