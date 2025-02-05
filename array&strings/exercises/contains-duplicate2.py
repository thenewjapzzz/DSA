class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False
            

solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))