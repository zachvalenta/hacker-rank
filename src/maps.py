def common_substring(s1, s2):
    for x in s1:
        if s2.find(x) > -1:
            return "YES"
    return "NO"
