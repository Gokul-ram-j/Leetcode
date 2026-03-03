class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preCrs={i:[] for i in range(numCourses)}

        for crs,preq in prerequisites:
            preCrs[crs].append(preq)
        
        visited=set()
        def solve(preq):
            if preq in visited:
                return False
            
            if preCrs[preq]==[]:
                return True
            
            visited.add(preq)

            for crs in preCrs:
                if solve(crs)==False:return False
            
            visited.remove(preq)

            return True

        
        for crs,preq in prerequisites:
            if solve(preq)==False: return False
        
        return True






