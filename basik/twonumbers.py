#!/usr/bin/python3
while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid input. Please enter numbers only.")

sum = num1 + num2
difference = num1 - num2
product = num1 * num2

if num2 == 0:
  quotient = "Division by zero is not allowed."
else:
  quotient = num1 / num2

# Print the results
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
