class SortLeetCode:
    def mergeNegSortedList(self, nums: list) -> list:
        if len(nums) == 0:
            return []
        if nums[0] >= 0:
            return nums

        for i, e in enumerate(nums):
            if e >= 0:
                break

        res = []
        l, r = i, i + 1
        print(f'l = {l}, r = {r}')
        while len(res) != len(nums):
            if l < 0:
                res.append(nums[r])
                r += 1
            elif r >= len(nums):
                res.append(abs(nums[l]))
                l -= 1
            elif abs(nums[l]) < nums[r]:
                res.append(abs(nums[l]))
                l -= 1
            else:
                res.append(nums[r])
                r += 1

        return res

if __name__ == '__main__':
    slc = SortLeetCode()
    print(slc.mergeNegSortedList([-1]))