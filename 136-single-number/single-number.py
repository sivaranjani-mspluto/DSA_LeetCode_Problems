class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hp={}
        for i in nums:
            if i in hp:
                hp[i]-=1
            else:
                hp[i]=1
        for j in hp:
            if hp[j]==1:
                return j
        return nums[0]