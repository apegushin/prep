from src.sliding_window import SlidingWindowLeetCode

class TestSlidingWindowLeetCode:
    def setup_method(self, method):
        self.swlc = SlidingWindowLeetCode()

    def test_mergeNegSortedList(self):
        assert self.swlc.minSubArrayLen(11, [1,2,3,4,5]) == 3
        assert self.swlc.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
