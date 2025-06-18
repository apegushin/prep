from typing import List

def minSubArrayLen_storage(target: int, nums: List[int]) -> int:
    """ leetcode #209 """

    sub = []
    i, sum = 0, 0
    while i < len(nums) and sum < target:
        sub.append(nums[i])
        sum += nums[i]
        i += 1

    if i == len(nums):
        if sum < target:
            return 0
        while sum - sub[0] >= target:
            e = sub.pop(0)
            sum -= e
        return len(sub)

    min_sz = len(sub)
    while i < len(nums):
        sub.append(nums[i])
        sum += nums[i]
        while sum - sub[0] >= target:
            e = sub.pop(0)
            sum -= e
        min_sz = min(min_sz, len(sub))
        i += 1
    return min_sz

def minSubArrayLen(target: int, nums: List[int]) -> int:
    """ leetcode #209 """

    min_sz = float('inf')
    l, r, sum = 0, 0, 0

    while r < len(nums):
        sum += nums[r]
        r += 1

        if sum >= target:
            while l < r and sum - nums[l] >= target:
                sum -= nums[l]
                l += 1
            min_sz = min(min_sz, r - l)

    return min_sz if min_sz < float('inf') else 0
