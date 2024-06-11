#!/usr/bin/python3
def fibonacci(n):

  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]

    # Generate the remaining Fibonacci numbers using iteration
    for i in range(2, n):
      next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
      fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Get user input with error handling
while True:
  try:
    n = int(input("Enter a positive integer (number of Fibonacci numbers): "))
    if n > 0:
      break  # Exit loop if input is valid (positive)
    else:
      print("Invalid input. Please enter a positive integer.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Generate and print the Fibonacci sequence
fibonacci_numbers = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

