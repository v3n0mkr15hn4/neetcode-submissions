class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            hashmap[sorted_s].append(s)
        result = list(hashmap.values())
        return result