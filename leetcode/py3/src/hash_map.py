from collections import Counter, defaultdict
from typing import List

def word_pattern(pattern: str, s: str) -> bool:
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

def find_the_difference(s: str, t: str) -> str:
    """ leetcode #389 """

    s_count, t_count = Counter(s), Counter(t)

    res = ''
    for k, v in t_count.items():
        if k not in s_count.keys() or v > s_count[k]:
            res = k
            break
    return res

def longest_consecutive(nums: List[int]) -> int:
    """ leetcode #128 """

    if len(nums) < 2: return len(nums)
    nums_set = set(nums)
    max_l = 1

    for num in nums_set:
        if num - 1 not in nums_set:
            i = 1
            while True:
                if num + i not in nums_set:
                    break
                i += 1
            max_l = max(max_l, i)
    return max_l

def fraction_to_decimal(numerator: int, denominator: int) -> str:
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

def find_repeated_dna_sequences(s: str) -> List[str]:
    """ leetcode #187 """

    res_set, seq_set = set(), set()
    if len(s) < 11: return list(res_set)

    for i in range(0, len(s) - 9):
        seq = s[i:i+10]
        if seq in seq_set:
            res_set.add(seq)
        else:
            seq_set.add(seq)
    return list(res_set)

def majority_element(nums: List[int]) -> List[int]:
    """ leetcode #229 """

    maj = len(nums) // 3
    res = []
    counters = defaultdict(int)
    for n in nums:
        counters[n] += 1
        if len(counters) == 3:
            new_counters = defaultdict(int)
            for n, c in counters.items():
                if c > 1:
                    new_counters[n] = c - 1
            counters = new_counters

    if len(counters) == 0:
        return res

    for c in counters.keys():
        count = 0
        for n in nums:
            if c == n:
                count += 1
        if count > maj:
            res.append(c)

    return res
