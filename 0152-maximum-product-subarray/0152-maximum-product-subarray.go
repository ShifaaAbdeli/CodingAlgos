func maxProduct(nums []int) int {
    
    n := len(nums)
    prefx := 1
    surffx := 1
    maxSub := nums[0]
    
    for i := 0; i < n; i++ {
        if prefx == 0 {
            prefx = 1
        } 
        if surffx == 0 {
            surffx = 1
        }
        prefx = prefx * nums[i]
        surffx = surffx * nums[n-1-i]
        maxSub = max(maxSub, prefx)
        maxSub = max(maxSub, surffx)
    }
    return maxSub
}