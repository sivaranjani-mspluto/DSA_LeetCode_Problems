class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #d={0:0,1:0,2:0}
        a,b,c=0,0,0
        for i,ele in enumerate(nums):
            if ele==0:
                a+=1
            elif ele==1:
                b+=1
            else:
                c+=1
        nums.clear()
        for i in range(0,a): nums.append(0)
        for i in range(0,b): nums.append(1)
        for i in range(0,c): nums.append(2)

        # k=0
        # for i in range(0,d[0]): nums.

        