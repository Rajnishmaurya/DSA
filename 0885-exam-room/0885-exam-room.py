class ExamRoom:

    def __init__(self, n: int):
        self.n=n
        self.students=[]
        

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0
        
        max_distance=self.students[0]

        seat_to_sit=0

        for i in range(len(self.students)-1):
            left=self.students[i]
            right=self.students[i+1]

            distance=(right-left)//2

            if distance>max_distance:
                max_distance=distance
                seat_to_sit=left+distance
        
        last_gap=(self.n-1)-self.students[-1]
        if last_gap>max_distance:
            maxi_distance=last_gap
            seat_to_sit=self.n-1
        
        insort(self.students,seat_to_sit)
        return seat_to_sit
        

    def leave(self, p: int) -> None:
        self.students.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)