from src.sort import SortLeetCode

class TestMatrixLeetCode:
    def setup_method(self, method):
        self.slc = SortLeetCode()

    def test_mergeNegSortedList(self):
        assert self.slc.mergeNegSortedList([-4, -1, 0, 1, 2, 3, 5, 6]) == [0, 1, 1, 2, 3, 4, 5, 6]
        assert self.slc.mergeNegSortedList([-12, -10, -8, -8, -5, -4, -1, 0, 1, 2, 3, 3, 5, 6]) == [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 8, 8, 10, 12]
        assert self.slc.mergeNegSortedList([]) == []
        assert self.slc.mergeNegSortedList([1, 2]) == [1, 2]
        assert self.slc.mergeNegSortedList([-1]) == [1]
        assert self.slc.mergeNegSortedList([0]) == [0]
        assert self.slc.mergeNegSortedList([-2, -1]) == [1, 2]
        assert self.slc.mergeNegSortedList([-2, -1, 0]) == [0, 1, 2]
        assert self.slc.mergeNegSortedList([0, 2, 4]) == [0, 2, 4]