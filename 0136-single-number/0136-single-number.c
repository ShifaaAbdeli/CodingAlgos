

int singleNumber(int* nums, int numsSize){
    
    int i, singleNum = 0;

    for(i = 0; i < numsSize; i++){
        singleNum = singleNum ^ nums[i];
    }
    return singleNum;
}