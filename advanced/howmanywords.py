#!/usr/bin/python3
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the name of the text file that is in the current directory: ")
    word_count = count_words_in_file(file_path)
    if word_count is not None:
        print(f"The number of words in the file is: {word_count}")

if __name__ == "__main__":
    main()
