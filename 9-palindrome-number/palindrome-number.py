class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        n=str(x)
        i=0
        j=len(n)-1
        while i<=j:
            if n[i]!=n[j]:return False
            i=i+1
            j=j-1
        return True   