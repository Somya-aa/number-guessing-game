import random

def play_game():
    print("\n🎮 Welcome to the Number Guessing Game!")

    print("\nChoose Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            max_num = 50
            break
        elif choice == "2":
            max_num = 100
            break
        elif choice == "3":
            max_num = 500
            break
        else:
            print("❌ Invalid choice. Try again.")

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {max_num}.")
    print("Can you guess it?\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("⬆️ Too low! Try again.\n")

            elif guess > secret_number:
                print("⬇️ Too high! Try again.\n")

            else:
                print(f"\n🎉 Congratulations!")
                print(f"You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Please enter a valid number.")

while True:
    play_game()

    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thanks for playing!")
        break