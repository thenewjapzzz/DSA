class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        _max = 1
        l, r = 0, 0
        counter = {}

        counter[s[0]] = 1

        while r < len(s) - 1:
            r+=1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            
            _max = max(_max, r-l+1)
        
        return _max
    
solution = Solution()
print(solution.maximumLengthSubstring('bcbbbcba'))