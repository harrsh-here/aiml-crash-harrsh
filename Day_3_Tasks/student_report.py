# Description: Defines a Student class with grading logic and tracks a global school name using a class variable.

class Student:
    school_name = "CIty School"

    def __init__(self, name: str, roll_no: int, marks: list[float]):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self) -> str:
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self) -> str:
        return f"School: {self.school_name} | Student: {self.name} (Roll: {self.roll_no}) | Avg: {self.average():.2f} | Grade: {self.grade()}"

if __name__ == "__main__":
    s1 = Student("Govind", 101, [85.0, 92.0, 88.0])
    s2 = Student("Dheeraj", 102, [70.0, 65.0, 78.0])
    s3 = Student("Gaurav", 103, [95.0, 98.0, 92.0])

    print(s1)
    print(s2)
    print(s3)