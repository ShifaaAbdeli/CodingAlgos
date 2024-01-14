class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ### Solution1- This approach is working but is not enought, 
        #need something like the below solution similar 
        #to the quickSelect
        #l = len(nums)
        #nums.sort()
        #return nums[l-k] # k is in order of 1 not 0

        ### Solution2- Using a similar approach to QuickSelect, 
        #which is similar to QuickSort approach 
        # Choise a pivot as the last element in the nums
        # compare each element of nums to pivot, only if it
        # is smaller than pivot, then swap it with the bigger
        # element at left side of pivot position, 
        # See QuickSort algo and see the sweapping below:
        
        #posK = len(nums) - k 
        #def quickSortKth(l, r):
        #    pivot = nums[r]
        #    leftP = l
        #    for i in range(l, r):
        #        if nums[i] <= pivot:
        #            nums[leftP], nums[i] = nums[i], nums[leftP]
        #            leftP += 1
        #    nums[leftP], nums[r] = nums[r], nums[leftP]

        #    if leftP > posK:
        #        return quickSortKth(l, leftP - 1)
        #    elif leftP < posK:
        #        return quickSortKth(leftP + 1, r)
        #    else:
        #        return nums[leftP]

        #return quickSortKth(0, len(nums) - 1)
        

        ### Solution3- Using MaxHeap by using Python3 minHeap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
        ## Time complexity is (k.log(n)), space O(1)


 