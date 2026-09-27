class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashdictS = {}

        for char in s:
            if char not in hashdictS:
                hashdictS[char] = 1
            else:
                hashdictS[char] += 1
        
        hashdictT = {}

        for char in t:
            if char not in hashdictT:
                hashdictT[char] = 1
            else:
                hashdictT[char] += 1
        
        return hashdictS == hashdictT