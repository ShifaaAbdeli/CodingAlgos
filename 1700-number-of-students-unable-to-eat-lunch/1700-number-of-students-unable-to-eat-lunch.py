class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0 # Student that didnt eat

        while count < len(students):
            if students[0] != sandwiches[0]:
                students.append(students[0])
                count += 1 # count the student didnt eat
            else:
                sandwiches.popleft()
                count = 0 # student eat a sandwishe

            students.popleft() # remove the students 
                               # that eat or back in the queue
        return len(students) # Student that never eat