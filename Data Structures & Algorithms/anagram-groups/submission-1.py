class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for i in strs:
            map_letters = [0]*26
            for j in i:
                map_letters[ord(j) - ord("a")] += 1
            words[tuple(map_letters)].append(i)
        
        return list(words.values())
            
                    