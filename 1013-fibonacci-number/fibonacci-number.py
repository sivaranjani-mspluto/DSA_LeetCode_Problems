#third=0
class Solution:
    def fib(self, n: int) -> int:
        third = 0
        dp=[-1]*7
        first=0
        second=1
        if n<=1:
            return n
        for i in range(2,n+1):
            third=first+second
            first=second
            second=third
        return third
