import src.sort as slc
import pytest

@pytest.mark.parametrize('nums, resNums',
                         [([-4, -1, 0, 1, 2, 3, 5, 6], [0, 1, 1, 2, 3, 4, 5, 6]),
                          ([-12, -10, -8, -8, -5, -4, -1, 0, 1, 2, 3, 3, 5, 6], [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 8, 8, 10, 12]),
                          ([], []),
                          ([1, 2], [1, 2]),
                          ([-1], [1]),
                          ([0], [0]),
                          ([-2, -1], [1, 2]),
                          ([-2, -1, 0], [0, 1, 2]),
                          ([0, 2, 4], [0, 2, 4]),
                         ])
def test_mergeNegSortedList(nums, resNums):
    assert slc.mergeNegSortedList(nums) == resNums

@pytest.mark.parametrize('nums1, m, nums2, n, expectedNums1',
                        [([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
                         ([1], 1, [], 0, [1]),
                         ([0], 0, [1], 1, [1]),
                        ])
def test_mergeTwoSortedListsInPlace(nums1, m, nums2, n, expectedNums1):
    slc.mergeTwoSortedListsInPlace(nums1, m, nums2, n)
    assert nums1 == expectedNums1

@pytest.mark.parametrize('intervals, result',
                        [([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
                         ([[1,4],[4,5]], [[1,5]]),
                        ])
def test_mergeIntervals(intervals, result):
    assert slc.mergeIntervals(intervals) == result

@pytest.mark.parametrize('citations, h',
                        [([3,0,6,1,5], 3),
                         ([1,3,1], 1),
                         ([100], 1),
                         ([100,100], 2),
                         ([0], 0),
                        ])
def test_hIndex(citations, h):
    assert slc.hIndex(citations) == h
