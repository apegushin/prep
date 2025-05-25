from typing import List

class SlidingWindowLeetCode:
    def minSubArrayLen_storage(self, target: int, nums: List[int]) -> int:
        sub = []
        i, sum = 0, 0
        while i < len(nums) and sum < target:
            sub.append(nums[i])
            sum += nums[i]
            i += 1

        if i == len(nums):
            if sum < target:
                return 0
            while sum - sub[0] >= target:
                e = sub.pop(0)
                sum -= e
            return len(sub)

        min_sz = len(sub)
        while i < len(nums):
            sub.append(nums[i])
            sum += nums[i]
            while sum - sub[0] >= target:
                e = sub.pop(0)
                sum -= e
            min_sz = min(min_sz, len(sub))
            i += 1
        return min_sz

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sz = float('inf')
        l, r, sum = 0, 0, 0

        while r < len(nums):
            sum += nums[r]
            r += 1

            if sum >= target:
                while l < r and sum - nums[l] >= target:
                    sum -= nums[l]
                    l += 1
                min_sz = min(min_sz, r - l)

        return min_sz if min_sz < float('inf') else 0


if __name__ == '__main__':
    swlc = SlidingWindowLeetCode()
    # print(swlc.minSubArrayLen1(11, [1,2,3,4,5]))
    print(swlc.minSubArrayLen1(7, [2,3,1,2,4,3]))