# Part A - Task 4
# Using *args to accept multiple numbers and return sum and average

def sum_and_average(*args):
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    if count == 0:
        return 0, 0
    average = total / count
    return total, average


# --- Testing ---
total, avg = sum_and_average(10, 20, 30, 40, 50)
print("Numbers: 10, 20, 30, 40, 50")
print("Sum:", total)
print("Average:", avg)

total2, avg2 = sum_and_average(5, 15, 25)
print("\nNumbers: 5, 15, 25")
print("Sum:", total2)
print("Average:", avg2)
