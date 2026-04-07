class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #have a pre[] for every course
        preMap={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            preMap[c].append(p)
        #{0:[1,2],1:[2,3]}
        visited=set()

        def dfs(c):
            if c in visited:
                return False
            if preMap[c]==[]:
                return True
            visited.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            preMap[c]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 
        