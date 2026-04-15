class Solution:
    def isUgly(self, n: int) -> bool:
        i=n
        while i>1:
            if i%2==0:
                i=i/2
            elif i%3==0:
                i=i/3
            elif i%5==0:
                i=i/5
            else:
                return False
        return  n>0