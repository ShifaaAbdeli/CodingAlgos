/*"""
Input: nums = [4,5,6,7,0,1,2], target = 0
1- B.F. approach: loop and check for target. Time O(n), space: O(1)

2- Two ptrs:
Input: nums = [4,5,6,7,0,1,2], target = 0
               l     mid     r
"""*/

func search(nums []int, target int) int {
    l := 0
    r := len(nums) - 1
    mid := 0
    
    for l <= r {
        mid = (l+r) // 2
        
        if nums[mid] == target {
            return mid
        }
        // Left part of the nums
        if nums[l] < nums[mid] {
            if target > nums[mid] || target < nums[l] {
                l = mid + 1
            } else {
                r = mid -1
            }
        // Right part of the nums
        } else {
            if target < nums[mid] || target > nums[r] {
                r = mid -1
            } else {
                l = mid + 1
            }
        }    
    }
    return -1
}