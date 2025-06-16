from collections import Counter
from typing import List

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

def longestConsecutive(nums: List[int]) -> int:
    """ leetcode #128 """

    if len(nums) < 2: return len(nums)
    numsSet = set(nums)
    maxL = 1

    for num in numsSet:
        if num - 1 not in numsSet:
            i = 1
            while True:
                if num + i not in numsSet:
                    break
                i += 1
            maxL = max(maxL, i)
    return maxL

def fractionToDecimal(numerator: int, denominator: int) -> str:
    """ leetcode #166 """

    if numerator == 0:
        return '0'

    res = ['-'] if (numerator < 0) ^ (denominator < 0) else []
    numerator, denominator = abs(numerator), abs(denominator)
    res.append(str(numerator // denominator))
    remainder = numerator % denominator
    if remainder == 0:
        return ''.join(res)

    res.append('.')
    num_hist = {}

    while remainder:
        if remainder in num_hist:
            res.insert(num_hist[remainder], '(')
            res.append(')')
            break
        num_hist[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator
    return ''.join(res)
