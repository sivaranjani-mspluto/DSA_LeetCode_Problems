class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursiveUtility(s,op,cp,n,res):
            if op==n and cp==n:
                res.append(s)
            if op<n :
                recursiveUtility(s+"(",op+1,cp,n,res)
            if cp<op:
                recursiveUtility(s+")",op,cp+1,n,res)
        res=[]
        s=""
        recursiveUtility(s,0,0,n,res)
        return res
