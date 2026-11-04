class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        log=dict(items1)
        for i in items2:
            item,weight=i
            log[item]=log.get(item,0)+weight
        return sorted(log.items())