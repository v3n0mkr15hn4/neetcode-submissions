class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        sorted_hashmap = sorted(hashmap, key = hashmap.get,reverse=True)
        result = list(sorted_hashmap)[:k]
        return result