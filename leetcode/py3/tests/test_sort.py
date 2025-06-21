import src.sort as slc
import pytest
from random import randint

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

@pytest.fixture
def random_list_20_items():
    return [randint(-100, 100) for _ in range(20)]

@pytest.mark.parametrize('nums, asc_sorted_nums',
                        [([], []),
                         ([1], [1]),
                         ([1,2], [1,2]),
                         ([2,-1], [-1,2]),
                         ([1,2,3], [1,2,3]),
                         ([3,1,2], [1,2,3]),
                         ([2,3,1], [1,2,3]),
                         ([2,1,3], [1,2,3]),
                         ([3,1,-2], [-2,1,3]),
                         ([-3,1,2], [-3,1,2]),
                         ([3,0,6,1,5], [0,1,3,5,6]),
                        ])
def test_allSortFunctions(nums, asc_sorted_nums, random_list_20_items):
    t2 = nums[:]
    slc.heapSort(t2)
    assert t2 == asc_sorted_nums
    nums_r = random_list_20_items
    t2r = nums_r[:]
    slc.heapSort(t2r)
    nums_r.sort()
    assert t2r == nums_r

    t3 = nums[:]
    slc.mergeSort(t3)
    assert t3 == asc_sorted_nums
    nums_r = random_list_20_items
    t3r = nums_r[:]
    slc.mergeSort(t3r)
    nums_r.sort()
    assert t3r == nums_r

    t4 = nums[:]
    slc.heapSortNoStorage(t4)
    assert t4 == asc_sorted_nums
    nums_r = random_list_20_items
    t4r = nums_r[:]
    slc.heapSortNoStorage(t4r)
    nums_r.sort()
    assert t4r == nums_r

@pytest.mark.parametrize('nums, num, idx',
                        [([1,2,3,5,6], 3, 2),
                         ([-3,-1,0,5,8,12], -3, 0),
                         ([0,1,3,5,6], 5, 3),
                        ])
def test_binarySearch(nums, num, idx):
    assert slc.binarySearch(nums, num) == idx

@pytest.mark.parametrize('nums, res',
                        [([1,1,1,2,2,3], 5),
                         ([0,0,1,1,1,1,2,3,3], 7),
                         ([], 0),
                         ([0], 1),
                         ([0,0], 2),
                         ([0,1], 2),
                         ([0,0,0,1,1,1], 4),
                         ([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1], 4),
                         ([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2], 5),
                         ([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2], 6),
                         ([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2], 6),
                         ([0,1,2,3,4,5,6,7,8], 9),
                        ])
def test_removeSecondDuplicates(nums, res):
    assert slc.removeSecondDuplicates(nums) == res

@pytest.mark.parametrize('nums, res',
                        [([3,4,5,1,2], 1),
                         ([4,5,6,7,0,1,2], 0),
                         ([11,13,15,17], 11),
                         ([1], 1),
                         ([1,2], 1),
                         ([2,1], 1),
                         ([1,2,3], 1),
                         ([3,1,2], 1),
                         ([2,3,1], 1),
                        ])
def test_findMinInRotatedSortedArray(nums, res):
    assert slc.findMinInRotatedSortedArray(nums) == res