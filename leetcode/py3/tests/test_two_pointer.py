import src.two_pointer as tplc
import pytest

@pytest.mark.parametrize('nums, combs',
                        [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
                         ([0, 0, 0], [[0, 0, 0]]),
                         ([-2, 0, 0, 2], [[-2, 0, 2]]),
                        ])
def test_threeSum(nums, combs):
    assert tplc.threeSum(nums) == combs

@pytest.mark.parametrize('nums, target, res',
                        [([-1, 2, 1, -4], 1, 2),
                         ([0, 0, 0], 1, 0),
                         ([-2, 0, 0, 2], 2, 2),
                         ([2, 5, 6, 7], 16, 15),
                        ])
def test_threeSumClosest(nums, target, res):
    assert tplc.threeSumClosest(nums, target) == res

@pytest.mark.parametrize('nums, res',
                        [([2,1,4,7,3,2,5], 5),
                         ([2,2,2], 0),
                         ([0], 0),
                         ([2, 3], 0),
                        ])
def test_longestMountain(nums, res):
    assert tplc.longestMountain(nums) == res

@pytest.mark.parametrize('nums, res',
                        [([],[]),
                         ([1],[1]),
                         ([2,1],[1,2]),
                         ([1,2],[2,1]),
                         ([3,2,1], [1,2,3]),
                         ([1,2,3], [3,2,1]),
                         ([6,4,3,1,0], [0,1,3,4,6]),
                         ([0,1,3,4,6], [6,4,3,1,0]),
                         ([6,4,3,2,1,0], [0,1,2,3,4,6]),
                         ([0,1,2,3,4,6], [6,4,3,2,1,0]),
                        ])
def test_reverseSortedList(nums, res):
    tplc.reverseSortedList(nums)
    # reversing sorted list in-place
    assert nums == res

@pytest.mark.parametrize('nums, res',
                        [([1,2,3], [1,3,2]),
                         ([3,2,1], [1,2,3]),
                         ([1,1,5], [1,5,1]),
                         ([6,2,1,5,4,3,0], [6,2,3,0,1,4,5]),
                         ([6,2,3,5,4,1,0], [6,2,4,0,1,3,5]),
                         ([4,6,5,2,1], [5,1,2,4,6]),
                        ])
def test_nextPermutation(nums, res):
    tplc.nextPermutation(nums)
    # permutation is built in-place
    assert nums == res
