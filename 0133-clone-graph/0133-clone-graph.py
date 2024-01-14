"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        #if not node: 
        #    return node

        #visited = {}
        #que = deque([node])
        # cloned the node and store it in hash map
        # next is to clone its neighbors, see below
        #visited[node] = Node(node.val, [])

        # Starting bfs traversal and clone 
        # the neigbors of each node in the grapgh
        #while que:
        #    n = que.popleft()
            # clone the node's "n" neighbors
        #    for nei in n.neighbors:
        #        if nei not in visited:
                    #clone each neighbor nei from neighbors list
        #            visited[nei] = Node(nei.val, [])
                    # put the nei in the bfd's que
        #            que.append(nei)
                    # Add the nei of the cloned node
                    # "visited[n]" to its cloned neighbors list
        #        visited[n].neighbors.append(visited[nei])

        # return the colned "visited[node] of the input node"
        #return visited[node]


        #### Approach of BFD traversal with adjList:
        ## 0- Note that adjList is the list of the lists of 
        ##    neighbors of nodes in the grapg respectively.
        ##    Meaning adjList[0] is list of nieghbors of 
        ##    node 1, adjList[1] is the list of neigbirs 
        ##    of node 2,...and so on ...
        ##
        ## 1- The deep copy or clone of a node n mean, 
        ##    to create a replica of a node in a separe 
        ##    datastructure, the clone need to maintine 
        ##    the value and list of neighbeurs of that 
        ##    giving node.
        ## 2- I create a visited hashMap data structure of 
        ##    type node (class Node) defined above.
        ##    where I can append a replica of each node 
        ##    n's neighbors. and tgen append it to the visited[n]
        ## 3- After bfs traversal is completed we return 
        ##    the visited.
        ####
        #queue = deque()
        #queue.append([node])
        # Part 1 from step 2 and 1 of the above. 
        # Define hashMap and clone the node n
        #visited = {}
        #visited[node] = Node(node.val, [])

        #while queue:
        #    n = queue.popleft()
        #    for nei in n.neighbors:
        #        if nei not in visited:
                    # clone each neighbor in hashMap visited[nei]
        #            visited[nei] = Node[nei.val, []]
        #            queue.append(nei)
            # Part2 of step2 and 1 of the above for each n (Node)
        #    visited[n].neighbors.append(visited[nei])

        # Step 3, return the hashMap created visited
        #return visted[node]

        ## Time complexity is O(m+n). Space O(n)

        ##### DFS Aproach ######
        cloneOldToNew = {}
        def dfs(node):
            if node in cloneOldToNew:
                return cloneOldToNew[node]
            # Make a copy of node.
            newNode = Node(node.val)
            cloneOldToNew[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode

        return dfs(node) if node else None

        ### Time complexity O(n), Space (n)

