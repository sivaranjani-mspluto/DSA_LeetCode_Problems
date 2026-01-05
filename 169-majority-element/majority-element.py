class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hp={}
        m=0
        for i in nums:
            if i not in hp:
                hp[i]=1
            else:
                hp[i]+=1
            m=max(m,hp[i])
        for j in hp:
            if hp[j]==m:
                return j
        return nums[0]