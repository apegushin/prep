from typing import List
import heapq

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

def binarySearch(nums: List[int], num: int) -> int:
    res = -1
    if len(nums) == 0: return res

    l, r = 0, len(nums) - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] == num:
            res = m
            break
        elif nums[m] > num:
            r = m - 1
        else:
            l = m + 1

    return res

def heapSort(nums: List[int]):
    if len(nums) < 2: return

    heapq.heapify(nums)
    nums_sorted = []
    while(nums):
        nums_sorted.append(heapq.heappop(nums))
    nums[:] = nums_sorted

def heapSortNoStorage(nums: List[int]):
    if len(nums) < 2: return

    def min_heapify_subtree(nums: List[int], i: int, n: int):
        l = 2*i + 1
        r = 2*i + 2
        largest = i

        if l < n and nums[l] > nums[largest]:
            largest = l

        if r < n and nums[r] > nums[largest]:
            largest = r

        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            min_heapify_subtree(nums, largest, n)

    for i in range(len(nums) // 2, -1, -1):
        min_heapify_subtree(nums, i, len(nums))

    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        min_heapify_subtree(nums, 0, i)

def mergeSort(nums: List[int]):
    if len(nums) < 2: return

    def split_merge(nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums[:]

        si = len(nums) // 2
        l = split_merge(nums[:si])
        r = split_merge(nums[si:])

        k = 0
        while l and r:
            if l[0] < r[0]:
                nums[k] = l[0]
                k += 1
                l.pop(0)
            else:
                nums[k] = r[0]
                k += 1
                r.pop(0)
        if l:
            for i in range(len(l)):
                nums[k] = l[i]
                k += 1
        elif r:
            for i in range(len(r)):
                nums[k] = r[i]
                k += 1
        return nums

    nums[:] = split_merge(nums)

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

def hIndex_sort(citations: List[int]) -> int:
    """ leetcode #274 """

    cur_h, max_h = 0, 0
    n = len(citations)
    if n == 0: return max_h

    citations.sort()
    for i in range(n - 1, -1, -1):
        cur_h = min(n - i, citations[i])
        max_h = max(max_h, cur_h)
    return max_h

def hIndex(citations: List[int]) -> int:
    """ leetcode #274 """

    res = 0
    n = len(citations)
    if n == 0: return res

    counts = [0] * (n + 1)
    for c in citations:
        counts[min(n, c)] += 1

    total_citations = 0
    for i in range(n, -1, -1):
        total_citations += counts[i]
        if i <= total_citations:
            res = i
            break
    return res

def removeSecondDuplicates(nums: List[int]) -> int:
    """ leetcode #80 """

    n = len(nums)
    if n < 2: return n
    slow = 1 if nums[1] == nums[0] else 0
    fast = slow + 1

    while fast < n:
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
            if fast < n and nums[fast] == nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
    return slow + 1
