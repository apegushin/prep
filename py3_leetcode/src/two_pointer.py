import math
from typing import List

def threeSum(nums: list[int]) -> list[list[int]]:
    """ leetcode #15 """

    res = []
    nums.sort()
    if nums[0] > 0:
        return res

    i = 0
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res

def threeSumClosest(nums: list[int], target: int) -> int:
    """ leetcode #16 """

    nums.sort()

    closest_sum = math.inf
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum = (nums[i] + nums[l] + nums[r])
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum

            if curr_sum == target:
                return int(closest_sum)
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
    return int(closest_sum)

def longestMountain_fromPeak(arr: List[int]) -> int:
    """ leetcode #845 """

    i, n = 1, len(arr) - 1
    res = 0

    while i < n:
        ls, rs = 0, 0
        li, ri = i - 1, i + 1
        while li >= 0 and arr[li] < arr[li+1]:
            ls += 1
            li -= 1

        while ri <= n and arr[ri] < arr[ri-1]:
            rs += 1
            ri += 1

        if ls > 0 and rs > 0:
            res = max(res, ls + 1 + rs)

        i = ri
    return res

def longestMountain(arr: List[int]) -> int:
    """ leetcode #845 """

    n = len(arr)
    if n == 0: return n

    leftSlope, rightSlope = [0] * n, [0] * n
    slopeLen, maxM = 0, 0

    for i in range(1, n):
        slopeLen = slopeLen + 1 if arr[i] > arr[i-1] else 0
        leftSlope[i] = slopeLen

    slopeLen = 0
    for j in range(n - 2, 0, -1):
        slopeLen = slopeLen + 1 if arr[j] > arr[j+1] else 0
        rightSlope[j] = slopeLen

    print(arr, leftSlope, rightSlope)

    for k in range(n):
        if leftSlope[k] > 0 and rightSlope[k] > 0:
            maxM = max(maxM, 1 + leftSlope[k] + rightSlope[k])

    return maxM
