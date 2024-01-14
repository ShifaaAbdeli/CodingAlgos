struct node {
    int key;
    int elemCount;
    struct node *next;
};

struct table {
    int size;
    struct node **list;
};

int hashCode (int size, int key) {
    
    if (key < 0) return (-(key%size));
    return (key%size);
}

struct table *HashMapCreate (int size) {
    int i;
    
    struct table* t = (struct table*)malloc(sizeof(struct table));
    t->list = (struct node**)malloc(sizeof(struct node *) * size);
    t->size = size;
    for (i=0; i<size; i++) {
        t->list[i] = NULL;
    }
    return t;
}

void hashMapInsert(struct table *t, int key, int val) {
    
    int pos = hashCode (t->size, key);
    struct node *list = t->list[pos];
    struct node *temp = list;
    
    while (temp) {
        if(temp->key == key) {
            temp->elemCount++;
            return;
        }
        temp = temp->next;
    }
    
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->key=key;
    newNode->elemCount=val;
    newNode->next = list;
    t->list[pos] = newNode;
}

int hashMapLookup(struct table *t, int key) {
    
    int pos = hashCode(t->size, key);
    struct node *list = t->list[pos];
    struct node *temp = list;
    while(temp) {
        if(temp->key == key) {
            return (temp->elemCount--);
        }
        temp = temp->next;
    }
    return -1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int i;
    struct table *t;
    
    if (nums2Size > nums1Size) {
        return (intersect(nums2, nums2Size, nums1, nums1Size, returnSize));
    }

    t = HashMapCreate (nums1Size);
    for(i=0; i < nums1Size; i++) {
        hashMapInsert(t, nums1[i], 1);
    }
    
    int *returnIntersect = malloc(sizeof(int) * nums1Size);
    
    *returnSize = 0;    
    for(i=0; i< nums2Size; i++) {
        if (hashMapLookup(t, nums2[i]) > 0) {
            returnIntersect[(*returnSize)++] = nums2[i];
        }        
    }
    //returnIntersect = (realloc(returnIntersect, sizeof(int) * (*returnSize)));
    return returnIntersect;
}