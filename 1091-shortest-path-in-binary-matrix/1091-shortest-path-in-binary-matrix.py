class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ### bfs traversal approach in a grid always 
        ### provide a short path.
        ### Here we travesrse via a grid.

        N = len(grid)  # The ROWS and COLS number are same
        #lenght = 1. # At the first check of (r, c), 
                    # the path lenght start as 1
        visited = set()
        queue = deque([(0, 0, 1)])
        visited.add((0,0))
        direction =[[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1], [0, -1], [0, 1]]

        while queue:
            row, col, lenght = queue.popleft()
            if row < 0 or row >= N or col < 0 or col >= N or grid[row][col] == 1:
                continue
            if row == N - 1 and col == N - 1:
                return lenght
            for dr, dc in direction:
                r, c = row + dr, col + dc
                if (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, lenght + 1))
        return -1

        ### Time complexity O(n**2), Space O(n**2)
