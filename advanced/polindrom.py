#!/usr/bin/python3
def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert the string to lowercase
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

def main():
    user_input = input("Enter a string: ")
    
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
