import re

# Regular expression pattern for matching mobile numbers
pattern = r"(\+?\d{1,3}[-.\s]?)?(\d{10})"

# Sample mobile numbers for testing
test_numbers = [
    "+91 9876543210",
    "9876543210",
    "+1-123-456-7890",
    "123-456-7890",
    "+91-9876543210",
    "987 654 3210"
]

# Checking each number against the pattern
for number in test_numbers:
    if re.fullmatch(pattern, number):
        print(f"{number} is a valid mobile number.")
    else:
        print(f"{number} is not a valid mobile number.")
