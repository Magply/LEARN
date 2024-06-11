#!/usr/bin/python3
def get_valid_numbers():
    while True:
        try:
            # Get input from the user as a string
            user_input = input("Enter a list of integers separated by spaces: ")

            # Split the string into individual values
            numbers_str = user_input.split()

            # Convert each string value to an integer
            numbers = [int(num) for num in numbers_str]

            # Return the valid list of integers
            return numbers
        except ValueError:
            # Handle invalid input (non-integer values)
            print("Invalid input. Please enter integers separated by spaces.")

# Get valid input from the user
numbers = get_valid_numbers()

# Print all elements in the list
print("Elements in the list:", numbers)

# Find the sum of all elements
total_sum = sum(numbers)
print("Sum of all elements:", total_sum)

# Find the maximum and minimum elements
max_value = max(numbers)
min_value = min(numbers)
print("Maximum element:", max_value)
print("Minimum element:", min_value)

