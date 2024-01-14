class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ### Usine simulation of max Heap from pythin min heap ###
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone2 > stone1:
                heapq.heappush(stones, stone1 - stone2)

        return -heapq.heappop(stones) if stones else 0

        ### Time complexity is O(nlog(n)). Space complexity is O(1)


        