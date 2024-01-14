typedef struct {
    int key;
    bool val_intersect;
    UT_hash_handle hh;
} utHashMap;

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){

    utHashMap *users = NULL, *temp, *s;
    int i, count = 0;
    int j = 0;
    int *intersection_result;
    
    //Popilate/ADD the hash table with the nums1 elements.
    for(i = 0; i < nums1Size; i++ ) {
        s = (utHashMap *)malloc(sizeof(utHashMap));
        s->key = nums1[i];
        s->val_intersect = false; // initialise the fase before search for it.
        HASH_ADD_INT(users, key, s);
    }
    
    //Search elements of nums2 in to the nums1's hash table and if found marke it to true.
    for(i = 0; i < nums2Size; i++) {
        s = NULL;
        HASH_FIND_INT(users, &nums2[i], s);
        if (s){
            s->val_intersect = true;
        }
    }
    *returnSize = nums1Size < nums2Size ? nums1Size: nums2Size;
    intersection_result = (utHashMap *)malloc(*returnSize *sizeof(int));
    
    HASH_ITER(hh, users, s, temp){
        if(s->val_intersect){
            intersection_result[j] = s->key;
            j++;
        }
    }
    *returnSize = j;
    return realloc(intersection_result, sizeof(int) * j);
}