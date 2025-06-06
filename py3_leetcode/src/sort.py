from typing import List

def mergeNegSortedList(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []
    if nums[0] >= 0:
        return nums

    for i, e in enumerate(nums):
        if e >= 0:
            break

    res = []
    l, r = i, i + 1 # type: ignore
    print(f'l = {l}, r = {r}')
    while len(res) != len(nums):
        if l < 0:
            res.append(nums[r])
            r += 1
        elif r >= len(nums):
            res.append(abs(nums[l]))
            l -= 1
        elif abs(nums[l]) < nums[r]:
            res.append(abs(nums[l]))
            l -= 1
        else:
            res.append(nums[r])
            r += 1

    return res

def mergeTwoSortedListsInPlace(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """ leetcode #88 """

    if n == 0: return

    i, j, k = m - 1, n - 1, n + m - 1
    while k >= 0:
        if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    """ leetcode #56 """

    intervals.sort(key=lambda x: x[0])

    def intersect(in1: List[int], in2: List[int]) -> bool:
        return in2[0] >= in1[0] and in2[0] <= in1[1]

    def mergeInto1st(in1: List[int], in2: List[int]):
        in1[0] = min(in1[0], in2[0])
        in1[1] = max(in1[1], in2[1])

    i = 0
    while i < len(intervals) - 1:
        if intersect(intervals[i], intervals[i+1]):
            mergeInto1st(intervals[i], intervals[i+1])
            intervals.pop(i + 1)
        else:
            i += 1

    return intervals

def hIndex(citations: List[int]) -> int:
    """ leetcode #274 """

    cur_h, max_h = 0, 0
    n = len(citations)
    if n == 0: return max_h

    citations.sort()
    for i in range(n - 1, -1, -1):
        cur_h = min(n - i, citations[i])
        max_h = max(max_h, cur_h)
    return max_h
