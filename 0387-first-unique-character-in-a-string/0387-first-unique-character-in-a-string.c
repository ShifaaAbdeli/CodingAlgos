int firstUniqChar(char* s) {
 
    int hashMapS[256] = {0};
    int i;
    int size = strlen(s);
    
    if (size == 1) {
        return 0;
    }
    
    for (i = 0; i < size; i++) {
        hashMapS[s[i]] += 1;
    }
    for (i=0; i < size; i++) {
        if (hashMapS[s[i]] == 1) {
            return i;
        }
    }
    return -1;
}