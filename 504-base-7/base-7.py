class Solution:
    def convertToBase7(self, num: int) -> str:
        if num<0:
            q=abs(num)
        elif num==0:
            return "0"
        else:
            q=num #q=100
        s=""
        while q:#100,14,
            s=str(q%7)+s
            q= q//7
        if num<0:
            return "-"+s
        return s

        