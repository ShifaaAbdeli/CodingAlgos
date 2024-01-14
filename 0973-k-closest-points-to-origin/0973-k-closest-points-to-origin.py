class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #### Using Min Heap Approach since we can use 
        #### Python heappify lib
        minHeap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        kClosest = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            kClosest.append([x,y])

        return kClosest

        ### Time complexity is O(klog(n)). 
        ### Space complexity is O(n)

