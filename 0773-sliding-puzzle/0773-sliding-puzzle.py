

from typing import List
from collections import deque

class Solution:
    #def slidingPuzzle(self, board: List[List[int]]) -> int:
        
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # WRITE YOUR BRILLIANT CODE HERE

        row_nums = len(board)
        col_nums = len(board[0])
        start = "".join([str(i) for row in board for i in row])
        target = "".join([str(i) for i in range(1, row_nums*col_nums)] + ["0"])
        #print(start, target)
        
        def swap(cur, i, j):
            buf = list(cur)
            buf[i], buf[j] = buf[j], buf[i]
            return "".join(buf)

        def get_neighbor(cur):

            delta_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            i = cur.find("0")
            row,col = int(i/col_nums), i%col_nums

            for i, j in delta_moves:
                yield row + i, col + j

        def bfs(start):

            num_steps = 0
            q = deque()
            q.append(start)
            visited = set()
            visited.add(start)
            print(visited)
            
            while(len(q) > 0):
                q_size = len(q)

                for _ in range(q_size):
                    cur = q.popleft()
                    #print(cur)
                    if cur == target:
                        return num_steps
                    for neighbor in get_neighbor(cur):
                        r, c = neighbor
                        if r < 0 or r >= row_nums or c < 0 or c >= col_nums:
                            continue
                        i = cur.find("0")
                        nxt_pos = swap(cur, i, r*col_nums + c)
                        if nxt_pos in visited:
                            continue
                        q.append(nxt_pos)
                        visited.add(nxt_pos)

                num_steps += 1

            return -1  
        
        return bfs(start)