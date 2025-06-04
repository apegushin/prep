import src.dp as dplc

def test_coinChange():
    assert dplc.coinChange_recursive([1,2,5], 11) == 3
    assert dplc.coinChange_recursive([2], 3) == -1
    assert dplc.coinChange_recursive([1], 0) == 0
    assert dplc.coinChange([1,2,5], 11) == 3
    assert dplc.coinChange([2], 3) == -1
    assert dplc.coinChange([1], 0) == 0

def test_climbStairs():
    assert dplc.climbStairs(2) == 2
    assert dplc.climbStairs(3) == 3
    assert dplc.climbStairs(4) == 5

def test_rob():
    assert dplc.rob([1,2,3,1]) == 4
    assert dplc.rob([2,7,9,3,1]) == 12
