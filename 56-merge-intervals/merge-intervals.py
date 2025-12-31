class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        mer=[]
        

        for i in intervals:
            if not mer or mer[-1][1] < i[0]:
                mer.append(i)
            else:
                mer[-1] = [ mer[-1][0] , max(mer[-1][1],i[1]) ] 

        return mer
