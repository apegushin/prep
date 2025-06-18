from collections import Counter
from functools import reduce
from typing import List, Optional
import re
import time
import heapq

def fstring_print():
    a, b = 10, 15
    print(f'{a + b = }')

def extract_words(paragraph: str) -> List[str]:
    res = []
    n = len(paragraph)
    if n == 0: return res
    i, w_b = 0, 0
    while i < n:
        while i < n and not paragraph[i].isalpha():
            i += 1
        if i < n:
            w_b = i
        while i < n and paragraph[i].isalpha():
            i += 1
        if i <= n:
            res.append(paragraph[w_b:i].lower())
    return res

def extract_words_re(paragraph: str) -> List[str]:
    return re.findall(r'\b[a-zA-Z]+\b', paragraph)

def extract_words_re_w(paragraph: str) -> List[str]:
    return re.findall(r'\w+', paragraph)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def commonChars(words: List[str]) -> List[str]:
    res_dict = reduce(lambda x, y: x & y, [Counter(w) for w in words])
    return [c for c, n in res_dict.items() for _ in range(n)]


if __name__ == '__main__':
    paragraph = "a, a, aaa, a, ba,b!,b,c!cc, c"
    print(extract_words(paragraph))
    print(extract_words_re(paragraph))
    print(extract_words_re_w(paragraph))
    print(commonChars(["bella","label","roller"]))