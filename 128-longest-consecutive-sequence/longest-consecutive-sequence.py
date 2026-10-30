class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sequence = set(nums)
        longest =0
        for i in sequence:
            #starting element
            if (i-1) not in sequence:
                length=0
                while (i+length) in sequence: #increase the sequence
                    length+=1
                longest = max(longest , length)
        return longest
                 
