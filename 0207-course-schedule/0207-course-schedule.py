class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMapAdjList = {i:[] for i in range(numCourses)}
        visited = set()

        for crs, prereq in prerequisites:
            preMapAdjList[crs].append(prereq)
        
        def dfs(crs):
            # Create hashMap for prerequite cources and
            # visited set for adjList and mark the visited cours
            if crs in visited: # Detecting a cycle
                return False
            if preMapAdjList[crs] == []:
                return True

            # Recursive dfs for each cours  
            visited.add(crs)
            for prereq in preMapAdjList[crs]:
                if not dfs(prereq): return False

            # Remove crs for visited set and 
            # clear hashMap for crs
            visited.remove(crs)
            preMapAdjList[crs] = []
            return True
        # main call for dfs recursive
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        #Time complexity O(m+n), space (m+n). 
        # m is number of cources, n is the number of prerequisite

            

         