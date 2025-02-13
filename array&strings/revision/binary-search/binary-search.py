class Solution:
    def binary_search(self, nums, k):
        lo = 0
        hi = len(nums)
        steps = 0

        while lo <= hi:
            steps += 1
            mid = int((lo+hi) / 2)

            if nums[mid] == k:
                print('steps', steps)
                return mid
            elif nums[mid] < k:
                lo = mid + 1
            else:
               hi = mid - 1
        
        return -1

solution = Solution()
print(solution.binary_search([1, 2, 3, 4, 5, 6, 7], 7))