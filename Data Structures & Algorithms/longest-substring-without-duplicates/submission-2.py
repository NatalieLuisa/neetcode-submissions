class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for r in s:
            while r in seen:
                seen.remove(s[left])
                left+=1
            seen.add(r)
            max_len = max(max_len, len(seen))
        return max_len
