from src.two_pointer import TwoPointerLeetCode

class TestTwoPointerLeetCode:
    def setup_method(self, method):
        print(f'setting up test for {method}')
        self.tplc = TwoPointerLeetCode()

    def test_threeSum(self):
        assert self.tplc.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
        assert self.tplc.threeSum([0, 0, 0]) == [[0, 0, 0]]
        assert self.tplc.threeSum([-2, 0, 0, 2]) == [[-2, 0, 2]]

    def test_threeSumClosest(self):
        assert self.tplc.threeSumClosest([-1, 2, 1, -4], 1) == 2
        assert self.tplc.threeSumClosest([0, 0, 0], 1) == 0
        assert self.tplc.threeSumClosest([-2, 0, 0, 2], 2) == 2
        assert self.tplc.threeSumClosest([2, 5, 6, 7], 16) == 15