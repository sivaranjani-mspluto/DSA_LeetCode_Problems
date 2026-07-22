class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp =prices[0]
        p=0
        for cp in prices[1:]:
            if cp<bp:
                bp=cp
            else:
                if (cp-bp) > p:
                    p=cp-bp 
        return p