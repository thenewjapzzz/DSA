class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, ch in enumerate(s):
            if not d.get(ch):
                d[ch] = [idx, 1]
            else:
                d[ch][1] += 1
        
        for ch, val in d.items():
            if val[1] == 1:
                return val[0]
            else:
                return -1
            
solution = Solution()
print(solution.firstUniqChar('lettcode'))