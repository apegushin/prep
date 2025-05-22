import math

class TwoPointerLeetCode:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        if nums[0] > 0:
            return res

        i = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest_sum = math.inf
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = (nums[i] + nums[l] + nums[r])
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return closest_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum


if __name__ == '__main__':
    tplc = TwoPointerLeetCode()
    # print(tplc.threeSumClosest([2, 5, 6, 7], 16))
