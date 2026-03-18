# Part C - Q2 Coding
# Student class with grade calculation and __str__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

    def __str__(self):
        grade = self.calculate_grade()
        return f"Student: {self.name} | Marks: {self.marks} | Grade: {grade}"


# --- Testing ---
s1 = Student("Alice", 92)
s2 = Student("Bob", 67)
s3 = Student("Charlie", 45)

print(s1)
print(s2)
print(s3)
