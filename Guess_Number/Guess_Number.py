import random

# გლობალური ცვლადები თამაშის სტატისტიკისთვის
total_guesses = 0   # ყველა თამაშისთვის მცდელობების მთლიანი რაოდენობა
game_count = 0      # ჩატარებული თამაშების რაოდენობა

def display_statistics():
    # აჩვენებს თამაშის სტატისტიკას: საშუალო მცდელობების რაოდენობა თითო თამაშზე.
    if game_count > 0:
        average_guesses = total_guesses / game_count
        print(f"\nYou guessed the number in an average of {average_guesses:.2f} attempts.")  # სტატისტიკის ჩვენება
    else:
        print("No games were played.")  # თუ არც ერთი თამაში არ ჩატარებულა

def get_valid_guess(range_max):
    # მოთამაშეს სთხოვს სწორი ფორმატით რიცხვის შეყვანას.
    while True:
        try:
            # ითხოვს რიცხვის შეყვანას მოცემული დიაპაზონის ფარგლებში
            guess = int(input(f"\nGuess a number between 1 and {range_max}: "))
            if 1 <= guess <= range_max:
                return guess  # ვალიდური რიცხვის დაბრუნება
            print(f"Please enter a number between 1 and {range_max}.")  # შეცდომის შეტყობინება
        except ValueError:
            # თუ მოთამაშემ შეიყვანა არა რიცხვი, არამედ ტექსტი
            print("Please enter a valid number!")  # შეცდომის შეტყობინება

def choose_difficulty():
    # მოთამაშეს აძლევს სირთულის არჩევის საშუალებას.
    while True:
        print("\nChoose a difficulty level:")
        print("1. Easy (1 to 10, 4 attempts)")     # მარტივი სირთულე
        print("2. Medium (1 to 50, 6 attempts)")   # საშუალო სირთულე
        print("3. Hard (1 to 100, 6 attempts)")    # რთული სირთულე

        choice = input("Enter the difficulty level (1/2/3): ")  # სირთულის არჩევის მოთხოვნა
        if choice == '1':
            return 10, 4  # მარტივი: დიაპაზონი 1-დან 10-მდე, 4 მცდელობა
        elif choice == '2':
            return 50, 6  # საშუალო: დიაპაზონი 1-დან 50-მდე, 6 მცდელობა
        elif choice == '3':
            return 100, 6  # რთული: დიაპაზონი 1-დან 100-მდე, 6 მცდელობა
        else:
            print("Invalid choice. Please try again.")  # არასწორი არჩევანი

def number_guessing_game():
    # თამაშის ძირითადი ლოგიკა.

    global total_guesses, game_count  # გლობალური ცვლადების გამოყენება სტატისტიკისთვის

    # მოთამაშის სახელის კითხვა და მისალმება
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's play a number guessing game!")

    # სირთულის არჩევა და თამაშის პარამეტრების განსაზღვრა
    range_max, guesses = choose_difficulty()
    number = random.randint(1, range_max)  # რანდომული რიცხვის ჩაფიქრება

    # თამაშის ძირითადი ციკლი
    while guesses > 0:
        guess = get_valid_guess(range_max)  # მოთამაშის შეყვანილი ვალიდური რიცხვის მიღება
        total_guesses += 1  # მცდელობების მთლიანი რაოდენობის გაზრდა

        if guess == number:
            # თუ მოთამაშემ გამოიცნო რიცხვი
            print("\nCongratulations, you guessed the number!")  # გამარჯვების შეტყობინება
            break
        elif guess > number:
            # თუ შეყვანილი რიცხვი მეტია ჩაფიქრებულზე
            print("Too high.")
        else:
            # თუ შეყვანილი რიცხვი ნაკლებია ჩაფიქრებულზე
            print("Too low.")
        
        guesses -= 1  # დარჩენილი მცდელობების შემცირება

    game_count += 1  # ჩატარებული თამაშების რაოდენობის გაზრდა
    print(f"The game is over. The number was: {number}")  # თამაშის დასრულების შეტყობინება

    # თამაშის სტატისტიკის ჩვენება
    display_statistics()

def main():
    # ძირითადი ფუნქცია, რომელიც აკონტროლებს თამაშის ციკლს.
    while True:
        number_guessing_game()  # თამაშის დაწყება
        play_again = input("\nDo you want to play again? (yes/no): ").lower()  # მოთამაშეს სთხოვს გაგრძელების არჩევას
        if play_again != 'yes':  # თუ მოთამაშეს არ სურს გაგრძელება
            print("\nThanks for playing! Goodbye!")  # დამშვიდობება
            break

# პროგრამის დაწყება
if __name__ == "__main__":
    main()
