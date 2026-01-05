class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap={}
        if len(s) != len(t):
            return False 
        for i in s:
            if i in hmap: 
                hmap[i]+=1
            else:
                hmap[i]=1
        for j in t:
            if j in hmap:
                hmap[j]-=1
            else:
                return False
        for e in hmap:
            if hmap[e]!=0:
                return False
        return True 
        