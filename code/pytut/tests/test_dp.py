from src.dp import DPLeetCode

class TestDPLeetCode:
    def setup_method(self, method):
        self.dplc = DPLeetCode()

    def test_coinChange(self):
        assert self.dplc.coinChange_recursive([1,2,5], 11) == 3
        assert self.dplc.coinChange_recursive([2], 3) == -1
        assert self.dplc.coinChange_recursive([1], 0) == 0
        assert self.dplc.coinChange([1,2,5], 11) == 3
        assert self.dplc.coinChange([2], 3) == -1
        assert self.dplc.coinChange([1], 0) == 0

    def test_climbStairs(self):
        assert self.dplc.climbStairs(2) == 2
        assert self.dplc.climbStairs(3) == 3
        assert self.dplc.climbStairs(4) == 5

