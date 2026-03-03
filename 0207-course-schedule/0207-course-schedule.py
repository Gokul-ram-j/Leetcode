class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preCrs={i:[] for i in range(numCourses)}

        for crs,preq in  prerequisites:
            preCrs[crs].append(preq)
        
        visited=set()
        
        def backtrack(crs):
            if crs in visited:
                return False
            
            if preCrs[crs]==[]:
                return True
            
            visited.add(crs)
            for preq in preCrs[crs]:
                if backtrack(preq)==False: return False
            visited.remove(crs)
            preCrs[crs]=[]
            return True

        for crs,preq in prerequisites:
            if backtrack(crs) ==False:
                return False
        
        return True