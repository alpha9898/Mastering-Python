import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

# Read the number of test cases
num_test_cases = int(input())

# Iterate through the test cases
for _ in range(num_test_cases):
    pattern = input()
    if is_valid_regex(pattern):
        print("True")
    else:
        print("False")
