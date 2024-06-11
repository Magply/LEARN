#!/usr/bin/python3
def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def count_vowels(s):
    vowels = "AEIOUaeiou"
    count = sum(1 for char in s if char in vowels)
    return count

def main():
    user_input = input("Enter a string: ")

    reversed_string = reverse_string(user_input)
    uppercase_string = to_uppercase(user_input)
    vowel_count = count_vowels(user_input)

    print(f"Reversed string: {reversed_string}")
    print(f"Uppercase string: {uppercase_string}")
    print(f"Number of vowels: {vowel_count}")

if __name__ == "__main__":
    main()
