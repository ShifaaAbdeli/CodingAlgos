class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # - MinHeap approach for this graph problem:
        # - use hashmap adjs for nodes neigbors
        # - use hashMap shortest for minTime path from each node to get the signal
        # - If can't get the signal to all node, return -1.

        adjs = {}
        for i in range(1, n+1):
            adjs[i] = []        
        #adjs = collections.defaultdict(list)

        for u, v, w in times:
            adjs[u].append((v, w))

        visit = set()
        minHeap = [(0, k)]
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in adjs[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return t if len(visit) == n else -1



        