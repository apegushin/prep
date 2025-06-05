from collections import Counter

def wordPattern(pattern: str, s: str) -> bool:
    """ leetcode #290 """

    n = len(pattern)
    words = s.split(' ')
    if len(words) != n: return False

    c2word = {}
    words_set = set()
    for i in range(n):
        if pattern[i] not in c2word:
            if words[i] in words_set:
                return False
            c2word[pattern[i]] = words[i]
            words_set.add(words[i])
        elif c2word[pattern[i]] != words[i]:
            return False
    return True

def findTheDifference(s: str, t: str) -> str:
    """ leetcode #389 """

    sCount, tCount = Counter(s), Counter(t)

    res = ''
    for k, v in tCount.items():
        if k not in sCount.keys() or v > sCount[k]:
            res = k
            break
    return res
