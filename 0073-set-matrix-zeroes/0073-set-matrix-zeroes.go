func setZeroes(matrix [][]int)  {
    
    ROW := len(matrix)
    COL := len(matrix[0])
    rowZero := false
    
    for r := 0; r < ROW; r++ {
        for c := 0; c < COL; c++ {
            if matrix[r][c] == 0 {
                matrix[0][c] = 0  
                if r > 0 {
                    matrix[r][0] = 0
                } 
                if r == 0 {
                    rowZero = true
                }
            }
        }
    }
    
    for r := 1; r < ROW; r++ {
        for c := 1; c < COL; c++ {
            if matrix[r][0] == 0 || matrix[0][c] == 0 {
                matrix[r][c] = 0
            }
        }
    }
    if matrix[0][0] == 0 {
        for r := 0; r < ROW;  r++ {
            matrix[r][0] = 0
        }
    }
    if rowZero == true {
        for c := 0; c < COL; c++ {
            matrix[0][c] = 0
        }
    }
}

//    Time complexity: O(nxm), Space: O(1)
