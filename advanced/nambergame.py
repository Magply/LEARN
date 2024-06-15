import random

def main():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get the user's guess
            guess = int(input("Guess a number between 1 and 100: "))
            
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            # Provide feedback
            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the right number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
