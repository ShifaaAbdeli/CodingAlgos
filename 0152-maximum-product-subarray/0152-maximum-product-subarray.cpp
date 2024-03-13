int max(int x, int y) {
    
    if (x > y) {
        return x;
    } else {
        return y;
    }
}

int maxProduct(int* nums, int numsSize) {
    int prefx = 1;
    int surffx = 1;
    int maxSub = nums[0];
        
    for (int i = 0; i < numsSize; i++) {
        if (prefx == 0) {
            prefx = 1;
        }
        if (surffx == 0) {
            surffx = 1;
        }
        
        prefx = prefx * nums[i];
        surffx = surffx * nums[numsSize -1-i];
        maxSub = max(maxSub, prefx);
        maxSub = max(maxSub, surffx);
    }
    return maxSub;
}