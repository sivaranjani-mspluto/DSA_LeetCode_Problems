class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums)-1
        # s1=0
        # s2=0
        # while l<r :
        #     s1 = s1+nums[l]
        #     s2 =s2+nums[r]
        #     if s1 == s2:
        #         return len(s1) + 1
        #     if s1 < s2:
        #         l+=1
        #     else:
        #         r-=1
        # return -1

        for i in range(len(nums)):
            s1 = sum(nums[:i])
            s2 = sum(nums[i+1:])
            if s1 == s2:
                return i
        return -1
