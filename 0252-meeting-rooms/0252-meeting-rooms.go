func canAttendMeetings(intervals [][]int) bool {
    // Sorting function for intervals
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][0] == intervals[j][0] {
            return intervals[i][1] < intervals[j][1]
        } else {
            return intervals[i][0] < intervals[j][0]
        }
    })
     
    for i := 0; i + 1 < len(intervals); i++ {
        if (intervals[i][1] > intervals[i+1][0]) {
            return false
        }
    }
    return true
}

// Time complexity: O(nlog(n)), space complexity: O(1)