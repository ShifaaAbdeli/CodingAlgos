/*
- Use of two pointers approach l and r:

1 - Use it for the case: a  b  c
                         ^^
                         lr
  - l and r start at same poistion i
  - then move l left and r ight
  
2 - Use it for the case: a b c
                         ^ ^
                         l r
  - l and r start at poistion l = i and r = i + 1
  - then move l left and r righ
*/

func countSubstrings(s string) int {
    L := len(s)
    countSub := 0
    
    for i := 0 ; i < L; i++ {
        l := i
        r := i
        // while condition for the case of Odd size of sub string
        for l >= 0 && r < L && s[l] == s[r] {
            countSub += 1
            l -= 1
            r += 1 
        }
        
        // while condition for the case of Odd size of sub string
        l = i
        r = i+1
        for l >= 0 && r < L && s[l] == s[r] {
            countSub += 1
            l -= 1
            r += 1
        }        
    }
    return countSub
}

// Time complexity O(n^2), Space: O(1)