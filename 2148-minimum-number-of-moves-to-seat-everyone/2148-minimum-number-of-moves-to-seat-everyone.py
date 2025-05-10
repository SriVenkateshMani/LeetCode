class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats = sorted(seats)
        students = sorted(students)
        for i, j in zip(seats, students):
            res += abs(i-j)
        return res