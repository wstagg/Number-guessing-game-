# This is a number guessing game where the user
# guesses a number between 1-100 in least tries possible.


from random import randint


score_list = []

# This fuction makes a list of the number of attempts you
# have and when called returns the lowest number.
def top_score(score):
    if len(score) > 0:
        best = score.sort()
        best = score.pop()
        print(f"Well done your top score is {best}. Try and beat it!")
    else:
        print("Sorry there are no scores to show yet.")

# This is the main body of the game.
def start_game():
    number = randint(1, 100)
    attempts = 0
    # print(number)
    print("Welcome to the number guessing game!")
    player_name = input("\nPlease enter your name:")
    ready_to_play = input(
        f"\nHello {player_name}, nice to meet you! Are you ready to play? enter yes/no:")
    while ready_to_play.lower() == "yes":
        try:
            guess = int(input("Guess a number between 1 and 100:"))
            if int(guess) < 1 or int(guess) > 100:
                raise ValueError("\nPlease choose a number between 1 and 100!")
            if guess == number:
                print("\nWell done, you guessed the number correctly!")
                attempts += 1
                score_list.append(attempts)
                print(f"\nYou took {attempts} attempts to guess the number correctly.")
                play_again = input("\nDo you want to play again? Enter yes/no:")
                attempts = 0
                if play_again == "no":
                    print("\nOkay, goodbye!")
                    break
                top_score(score_list)
            elif guess < number:
                print("\nYour guess was too low! Try again.")
                attempts += 1
            elif guess > number:
                print("\nYour guess was too high! Try again.")
                attempts += 1
        except ValueError:
            print("\nOops that wasnt a valid guess. Try again!")
    else:
        print("\nNo problem, see you again soon")


if __name__ == "__main__":
    start_game()
