class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        for i,ele in enumerate(nums):
            if ele==0:
                d[0]+=1
            elif ele==1:
                d[1]+=1
            else:
                d[2]+=1
        nums.clear()
        for i in range(0,d[0]): nums.append(0)
        for i in range(0,d[1]): nums.append(1)
        for i in range(0,d[2]): nums.append(2)

        