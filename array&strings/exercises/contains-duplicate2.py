class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for idx, num in enumerate(nums):
            if num in d and idx - d[num] <= k:
                return True
            d[num] = idx
        
        return False

solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
        