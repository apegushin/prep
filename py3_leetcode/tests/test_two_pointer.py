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
                         ([2, 3], 0)
                        ])
def test_longestMountain(nums, res):
    assert tplc.longestMountain(nums) == res
