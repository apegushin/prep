from typing import List

class DPLeetCode:
    def coinChange_recursive(self, coins: List[int], amount: int) -> int:
        memo = {}
        def minCoins(amount: int):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            else:
                cm = float('inf')
                for c in coins:
                    if (amount - c) not in memo:
                        memo[amount - c] = minCoins(amount - c)
                    if memo[amount - c] >= 0 and memo[amount - c] < cm:
                        cm = memo[amount - c]
                return cm + 1 if cm < float('inf') else -1

        return minCoins(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        steps = [0 for i in range(amount + 1)]

        for i in range(1, amount + 1):
            cm = float('inf')
            for c in coins:
                if i - c >= 0 and steps[i - c] >= 0:
                    cm = min(cm, steps[i - c] + 1)
            steps[i] = cm if cm < float('inf') else -1

        return steps[amount]

    def climbStairs(self, n: int) -> int:
        steps = [1] * (n + 1)
        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]