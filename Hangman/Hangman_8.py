import random

# სიტყვების სია, რომელიც შეიცავს რამდენიმე ყველაზე გავრცელებულ ქართულ სახელს
WORD_LIST = ['giorgi', 'davit', 'aleksandre', 'luka', 'nikolozi', 'nino', 'mariami', 'ana', 'tamari', 'maia']

def choose_word(word_list):
    """არჩევს შემთხვევით სიტყვას მოცემული სიტყვების სიიდან."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """
    აჩვენებს სიტყვის სტატუსს.
    გამოცნობილი ასოები ნაჩვენებია, ხოლო დანარჩენები ჩანაცვლებულია ქვედა ხაზით.
    """
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_guess(already_guessed):
    """
    მომხმარებლისგან იღებს ახალ ასოს.
    უზრუნველყოფს, რომ შეყვანილი ასო იყოს ვალიდური და არ განმეორდეს.
    """
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) == 1 and guess.isalpha() and guess not in already_guessed:
            return guess
        print(f'Invalid input or already guessed. Try again.')

def play_hangman(total_score):
    """
    თამაშის ძირითადი ლოგიკა.
    მოიცავს სიტყვების არჩევას, მომხმარებლის ნაბიჯების დამუშავებას, 
    ქულების დათვლას და შედეგების ჩვენებას.
    """
    word = choose_word(WORD_LIST)  # შემთხვევით აირჩევა სიტყვა
    guessed_letters = set()  # მომხმარებლის გამოცნობილი ასოების ნაკრები
    incorrect_guesses = set()  # მომხმარებლის არასწორი ასოების ნაკრები
    max_attempts = len(word)  # მცდელობების მაქსიმალური რაოდენობა განისაზღვრება სიტყვის სიგრძით
    score = 0  # ამ თამაშის ქულა

    print('Welcome to Hangman!')  # მისალმება
    print(f'You have {max_attempts} attempts to guess one of the most common Georgian names.\n')

    while len(incorrect_guesses) < max_attempts:
        # მიმდინარე სიტყვის და მცდელობების სტატუსის ჩვენება
        print(f'Word: {display_word(word, guessed_letters)}')
        print(f'Remaining attempts: {max_attempts - len(incorrect_guesses)}')
        print(f'Incorrect guesses: {", ".join(sorted(incorrect_guesses)) or "None"}')
        print(f'Your score for this game: {score}')
        print(f'Total score: {total_score}\n')

        # ახალი ასოს მიღება
        guess = get_guess(guessed_letters | incorrect_guesses)

        if guess in word:
            guessed_letters.add(guess)  # გამოცნობილი ასოს დამატება
            points = word.count(guess) * 10
            score += points  # ქულების მომატება
            total_score += points  # საერთო ქულების განახლება
            print(f'Good guess! "{guess}" is in the word.')
            if guessed_letters == set(word):  # თუ ყველა ასო სწორად გამოიცნო
                print(f'Congratulations! You guessed the word: "{word}"!')
                break
        else:
            incorrect_guesses.add(guess)  # არასწორი ასოს დამატება
            score -= 5  # ქულების შემცირება
            total_score -= 5  # საერთო ქულების განახლება
            print(f'Incorrect guess: "{guess}".')

    else:
        # თამაშის დასრულება მცდელობების ამოწურვის შემთხვევაში
        print(f'\nGame over! The word was "{word}".')

    print(f'Your total score is now: {total_score}\n')
    return total_score

def main():
    # ძირითადი ფუნქცია, რომელიც აკონტროლებს თამაშის ციკლს.
    total_score = 0  # საწყისი ქულა ყველა თამაშისთვის
    while True:
        total_score = play_hangman(total_score)  # თამაშის დაწყება და ქულების განახლება
        play_again = input("\nDo you want to play again? (yes/no): ").lower()  # მოთამაშეს სთხოვს გაგრძელების არჩევას
        if play_again != 'yes':  # თუ მოთამაშეს არ სურს გაგრძელება
            print(f"\nThanks for playing! You have scored '{total_score}' points. Goodbye!")  # დამშვიდობება
            break

# პროგრამის დაწყება
if __name__ == "__main__":
    main()
