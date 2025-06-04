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
    l, r = i, i + 1
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
