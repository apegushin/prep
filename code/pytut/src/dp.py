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
