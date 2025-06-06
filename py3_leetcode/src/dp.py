from typing import List

def coinChange_recursive(coins: List[int], amount: int) -> int:
    """ leetcode #322 """

    memo = {}
    def minCoins(amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        else:
            cm = float('inf')
            for c in coins:
                if (amount - c) not in memo:
                    memo[amount - c] = minCoins(amount - c)
                if memo[amount - c] >= 0 and memo[amount - c] < cm:
                    cm = memo[amount - c]
            return cm + 1 if cm < float('inf') else -1  # type: ignore

    return minCoins(amount)

def coinChange(coins: List[int], amount: int) -> int:
    """ leetcode #322 """

    steps = [0 for i in range(amount + 1)]

    for i in range(1, amount + 1):
        cm = float('inf')
        for c in coins:
            if i - c >= 0 and steps[i - c] >= 0:
                cm = min(cm, steps[i - c] + 1)
        steps[i] = cm if cm < float('inf') else -1 # type: ignore

    return steps[amount]

def climbStairs(n: int) -> int:
    """ leetcode #70 """

    steps = [1] * (n + 1)
    for i in range(2, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2]
    return steps[n]

def rob(nums: List[int]) -> int:
    """ leetcode #198 """

    n = len(nums)
    if n < 3:
        return max(nums)

    partials = [nums[0], nums[1], nums[0] + nums[2]]
    for i in range(3, n):
        partials.append(nums[i] + (max(partials[i - 2], partials[i - 3])))
        print(partials)
    return max(partials[n - 1], partials[n - 2])

def wordBreak(s: str, wordDict: List[str]) -> bool:
    """ leetcode #139 """

    if len(s) == 0: return False

    flags = [x == 0 for x in range(len(s) + 1)]
    for i in range(len(s)):
        if flags[i]:
            for w in wordDict:
                if len(w) <= len(s[i:]) and s[i:].startswith(w):
                    flags[i + len(w)] = True

    return flags[len(s)]
