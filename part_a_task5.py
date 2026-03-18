# Part A - Task 5
# Using **kwargs to accept student names and marks, return top student

def top_student(**kwargs):
    best_name = None
    best_marks = None
    for name, marks in kwargs.items():
        if best_marks is None or marks > best_marks:
            best_marks = marks
            best_name = name
    return best_name, best_marks


# --- Testing ---
name, marks = top_student(Alice=85, Bob=92, Charlie=78, Diana=96, Eve=88)
print("Students: Alice=85, Bob=92, Charlie=78, Diana=96, Eve=88")
print(f"Top student: {name} with {marks} marks")
