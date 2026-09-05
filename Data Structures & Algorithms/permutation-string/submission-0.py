class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1Map = {}
            for i in s1:
                s1Map[i] = 1 + s1Map.get(i, 0)
            
            for l in range(len(s2) - len(s1) + 1):
                s2Map = {}
                for i in s2[l:l + len(s1)]:
                    s2Map[i] = 1 + s2Map.get(i, 0)
                if s1Map == s2Map:
                    return True
            return False