# Part A - Task 1
# Find max, min using loops and count frequency using dictionary

def find_max_min(lst):
    # start with first element as both max and min
    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# --- Testing ---
numbers = [3, 7, 2, 9, 4, 7, 3, 1, 9, 9]

max_val, min_val = find_max_min(numbers)
print("List:", numbers)
print("Maximum:", max_val)
print("Minimum:", min_val)

freq = count_frequency(numbers)
print("Frequency:", freq)
