class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for idx, num in enumerate(nums):
            if num in d:
                return [d[num], idx]
            d[target - num] = idx


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
