class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #process the bar with the lower height first
        l,r=0,len(height)-1
        maxl,maxr,twater=0,0,0
        while l<=r:
            if height[l]<=height[r]:
                if height[l]>=maxl:
                    maxl=height[l]
                else :
                    twater+=maxl-height[l]
                l+=1
            else:
                if height[r]>=maxr:
                    maxr=height[r]
                else:
                    twater += maxr-height[r]
                r-=1
        return twater