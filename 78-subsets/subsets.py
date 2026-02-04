class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]

        def backtrack(i): #i is the index
            if i == n: #if our index is out of bounds
                res.append(sol[:]) #add a copy of the "sol" to the res[]
                return 
            #don't pick nums[i]
            backtrack(i+1) #move on

            #pick nums[i]
            sol.append(nums[i]) #pick the nums[i]
            backtrack(i+1) #deal with the nums[i] and move on
            sol.pop() #to UNDO the decision of picking the nums[i]

        backtrack(0) #started at 1st index
        return res