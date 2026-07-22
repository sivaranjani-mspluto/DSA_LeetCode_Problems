class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hmap={}
       for i,cnum in enumerate(nums):
        if target-cnum in hmap:
            return [i,hmap[target-cnum]]
        else:
            hmap[cnum] =i


        