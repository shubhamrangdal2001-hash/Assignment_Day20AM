# Part A - Task 2
# Reverse a number and check palindrome using while loop

def reverse_number(n):
    reversed_num = 0
    n = abs(n)  # handle negatives
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num


def is_palindrome(n):
    original = abs(n)
    rev = reverse_number(original)
    return original == rev


# --- Testing ---
num = 12321
print(f"Reversed {num} -> {reverse_number(num)}")
print(f"Is {num} a palindrome? {is_palindrome(num)}")

num2 = 123
print(f"Reversed {num2} -> {reverse_number(num2)}")
print(f"Is {num2} a palindrome? {is_palindrome(num2)}")
