class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            L = arr[l:m+1]
            R = arr[m+1: r+1]
            # Use two pointer approach to sort the 
            # two sub arrays in one array
            i, j, k = l, 0, 0
            while j < len(L) and k < len(R):
                if L[j] < R[k]:
                    arr[i] = L[j]
                    j += 1
                else:
                    arr[i] = R[k]
                    k += 1
                i += 1
            while j < len(L):
                arr[i] = L[j]
                j += 1
                i += 1
            while k < len(R):
                arr[i] = R[k]
                k += 1
                i += 1

        # MergeSort will split the arr in to two sub array
        # recursively down to single element per each of 
        # the two sub arrays.
        # Then call merge function above to merge the 
        # two array in a single sorted array
        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l+r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)