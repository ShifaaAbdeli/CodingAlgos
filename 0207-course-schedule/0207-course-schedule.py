"""
numCourses = []
ai ---> bi, ci, di, ... ; preMap[ai] = [bi, ci, di, ...]

- check special cases: numCources = []
- build perMap of lists of all preRecusite of each crs 
- check if cource visited
- dfs traversal to check pre-recusite can be taking truly
- check all cources schedule with dfs and return true if all completed or fasle

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set()
        
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
## Time complexity: O(numCourses^2); Space: O(numCources)