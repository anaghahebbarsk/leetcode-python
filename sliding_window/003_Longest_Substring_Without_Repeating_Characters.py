# Time complexity: O(N)
# space complexity: O(min(n, charset))
# LeetCode 3: Longest Substring Without Repeating Characters
# Approach: Sliding Window + Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in c :
                c.remove(s[l])
                l += 1
            c.add(s[r])
            res = max(res,r-l+1)
        return res

        