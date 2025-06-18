import src.sliding_window as swlc
import pytest

@pytest.mark.parametrize('target, nums, min_sz',
                        [(11, [1,2,3,4,5], 3),
                         (7, [2,3,1,2,4,3], 2),
                        ])
def test_mergeNegSortedList(target, nums, min_sz):
    assert swlc.minSubArrayLen(target, nums) == min_sz
