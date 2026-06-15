class Solution:
    def reverseWords(self, s: str) -> str:
        l= s.split()
        rl= l[::-1]
        #print(rl)
        return " ".join(rl)