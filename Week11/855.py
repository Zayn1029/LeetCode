class ExamRoom:
    def __init__(self, n):
        self.n = n
        self.students = []

    def seat(self):
        if not self.students:
            self.students.append(0)
            return 0
        
        max_dist = self.students[0]
        best_seat = 0
        
        for i in range(1, len(self.students)):
            left = self.students[i-1]
            right = self.students[i]
            dist = (right - left) // 2
            
            if dist > max_dist:
                max_dist = dist
                best_seat = left + dist
        
        if self.n - 1 - self.students[-1] > max_dist:
            max_dist = self.n - 1 - self.students[-1]
            best_seat = self.n - 1
        
        pos = 0
        while pos < len(self.students) and self.students[pos] < best_seat:
            pos += 1
        
        self.students.insert(pos, best_seat)
        return best_seat

    def leave(self, p):
        self.students.remove(p)