class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1Map = {}
            s2Map = {}
            for i in s1:
                s1Map[i] = 1 + s1Map.get(i, 0)
            l = 0
            for r in range(len(s1)-1,len(s2)):
                for i in s2[l:r+1]:
                    s2Map[i] = 1 + s2Map.get(i,0)
                if s1Map == s2Map:
                    return True
                else:
                    l += 1
                    s2Map.clear()
            return False
