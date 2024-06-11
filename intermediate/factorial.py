#!/usr/bin/python3
def factorial(number):

  if number < 0:
    raise ValueError("Factorial is not defined for negative numbers.")

  # Base case: factorial of 0 is 1
  if number == 0:
    return 1

  # Recursive case: factorial(n) = n * factorial(n-1)
  else:
    return number * factorial(number - 1)

# Get user input with error handling
while True:
  try:
    number = int(input("Enter a non-negative integer: "))
    if number >= 0:
      break  # Exit the loop if input is valid (non-negative)
    else:
      print("Invalid input. Please enter a non-negative integer.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Calculate and print the factorial
result = factorial(number)
print(f"The factorial of {number} is {result}.")
