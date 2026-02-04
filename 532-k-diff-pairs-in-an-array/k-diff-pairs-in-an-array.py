class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        answ=0
        d={}
        for x in nums:
            if x in d: d[x]+=1
            else:      d[x]=1
        
        if k>0 :
            for x in d.keys():
                if x+k in d: answ+=1
            #answ=sum(x+k in d for x in d.keys())
        elif k==0: 
            for x in d.values():
                if x>1: answ+=1
            #answ=sum(k>1 for k in d.values())
        else: return 0
                
        return answ