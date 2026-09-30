class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        
        sorted_nums = sorted(countMap, key=lambda num: countMap[num], reverse=True)

        return sorted_nums[:k]