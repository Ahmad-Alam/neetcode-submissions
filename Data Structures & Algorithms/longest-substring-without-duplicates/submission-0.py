class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ''
        result = 0
        for i in range(len(s)):
            if s[i] in current:
                current = current.split(s[i])[1] + s[i]
            else:
                current += s[i]
            if len(current) > result:
                result = len(current)
        return result