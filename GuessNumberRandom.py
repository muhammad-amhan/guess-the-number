# Author: Muhammad Amhan
# Date: 20/06/2018
# Email: muhammadamhan@gmail.com
# PROBLEMS -> Passed all tests.
# IMPROVEMENTS -> No suggestions yet.
import random

# Initialise variables:
highest = 10  # Highest number to guess from.
attempts = 4  # Up to three attempts.
computerName = "Megatron"  # Computer name for vs computer mode.
# List of possible user input / used when asking whether to play again or not.
yes_list = ['yes', 'Yes', 'YES', 'y', 'Y']
no_list = ['No', 'no', 'n', 'NO', 'N']

print("Hi, welcome to my first game in Python!\n"
      "Rules are simple:\n"
      "     1) Be over 10 years old.\n"
      "     2) Select a game mode.\n"
      "     3) Guess the number between 1 and 10, first to guess, wins! ** NOTE ** hints will be given. ;)\n"
      "That's it! Select your opponent and start playing...\n"
      ".......................................\n"
      "** CHALLENGE ** - can you beat Megatron?")
# Loop the game. if the player in human vs human mode decides to
# change game mode because player 2 isn't old enough...
while True:
    # Select game mode.
    game_mode = int(input(".......................................\n"
                          "Game Mode: \n"
                          "1 -- Human vs Megatron (Computer)\n"
                          "2 -- Human vs Human\n"
                          "3 -- Quit\n"))

    number = random.randint(1, highest)  # The number is between 1 and 10.
    computerGuess = random.randint(1, highest)  # This is the number the computer guesses in human vs computer mode.
    # Exit the game.
    if game_mode == 3:
        print(".......................................\n"
              "See you soon, bye!\n"
              ".......................................")
        break  # Terminate the game, stop processing while loop.

    # Otherwise continue and request player name.
    username = input("Player Name: ")
    # Make sure name is not an empty string, otherwise break the loop and continue.
    while True:
        if username == '':
            print("Player must have a name...")
            username = input("Player Name: ")
        else:
            break  # Exit while loop.

    # Make sure age field is not empty and the correct data type is passed (integer).
    while True:
        try:
            while True:
                age = int(input("How old are you, {0}? ".format(username)))  # The user's age (must be 18 or over).
                if (age < 1) or (age > 130):
                    print("Real age required!")
                else:
                    break  # Exit while loop.
            break  # Break from try.
        except ValueError:
            print("{0}, you must have an age!".format(username))
    # Players must be 10+ years old.
    if age >= 10:
        # If vs computer is selected:
        if game_mode == 1:
            # While to continuously check for input data.
            while True:
                print("\nGame Started:")
                attemptCount = 1  # Initial attempt.
                print("->> {0} (attempt {1}): {2}".format(computerName, attemptCount, computerGuess))

                while True:
                    try:
                        usr_answer = int(input("->> {0} (attempt {1}): ".format(username, attemptCount)))
                        #  Start loop three times, for three attempts.
                        for attemptCount in range(attemptCount, attempts):
                            # If the computer and user guessed it together:
                            if usr_answer == computerGuess == number:
                                print("\n** Hey, it's a DRAW, well done to both of you. The answer is ({0}). **"
                                      .format(number))
                                break  # Exit for loop.

                            # If user guessed it:
                            if usr_answer == number:
                                print("\n** Congratulations {0}, it is ({1}). "
                                      "You've beaten Megatron in {2} attempt(s). **"
                                      .format(username, number, attemptCount))
                                break  # Exit for loop.

                            # If computer guessed it:
                            if computerGuess == number:
                                print("\n** Sorry {0}, {1} guessed it correctly. It's ({2}). **"
                                      .format(username, computerName, number))
                                break  # Exit for loop.

                            # Display a reminder message to the user that it's their last guess attempt
                            if attemptCount == 2 and usr_answer != number:
                                print("\n** Oh it's the last chance for both of you.. **".format(username))

                            # If the loop never satisfies any condition after three attempts:
                            # I wanted a way to loop three times (without running the fourth iteration)
                            # The problem was, when looping 4 times, 3 attempts count but the fourth attempt
                            # is also printed but not counted. This solved it, now the fourth isn't printed...
                            if attemptCount == 3 and usr_answer != number != computerGuess:
                                print("\n** Sorry {0} and {1}, but you both lost! The number is ({2}). **"
                                      .format(username, computerName, number))
                                break  # Exit for loop.
                            # If answer is not correct:
                            else:
                                attemptCount += 1  # Increment number of attempts.
                                # If computer guess is less than the number.
                                if computerGuess < number:
                                    print("\n{0}, please guess higher than ({1})."
                                          .format(computerName, computerGuess))
                                    # Computer guesses higher than what it guessed.
                                    computerGuess = random.randint((computerGuess + 1), highest)
                                    print("->> {0}, (attempt {1}): {2}"
                                          .format(computerName, attemptCount, computerGuess))

                                # If it's greater than the number.
                                else:
                                    print("\n{0}, please guess less than ({1})."
                                          .format(computerName, computerGuess))
                                    # Computer Guesses less than what it guessed.
                                    computerGuess = random.randint(1, (computerGuess - 1))
                                    print("->> {0}, (attempt {1}): {2}"
                                          .format(computerName, attemptCount, computerGuess))

                                # If user guess is less than the number.
                                if usr_answer < number:
                                    print("{0}, please guess higher than ({1})."
                                          .format(username, usr_answer))
                                    usr_answer = int(input("->> {0}, (attempt {1}): "
                                                           .format(username, attemptCount)))

                                # If it's greater than the number.
                                else:
                                    print("{0}, please guess less than ({1})."
                                          .format(username, usr_answer))
                                    usr_answer = int(input("->> {0}, (attempt {1}): "
                                                           .format(username, attemptCount)))
                    # Exception if value is not integer.
                    except ValueError:
                        print("{0}, choose a number...".format(username))
                        continue
                    else:
                        break  # Break from while loop
                break  # Break while loop following the age condition

        # If game mode is vs another human:
        else:
            username2 = input("\nPlayer2 Name: ")
            while True:
                if username2 == '':
                    print("Player2 must have a name...")
                    username2 = input("Player2 Name: ")
                # Make sure players don't have same username.
                elif username2 == username:
                    print("Name already taken.")
                    username2 = input("Player2 Name: ")
                else:
                    break  # Exit while loop.
            # This while loop is for try and exception repetition/check.
            while True:
                try:
                    # I think I don't need this while loop! while True:
                    age2 = int(input("How old are you, {0}? ".format(username2)))
                    if (age2 < 1) or (age2 > 130):
                        print("Real age required!")
                    else:
                        break  # Breaks from try.
                    # break or this break
                except ValueError:
                    print("{0}, you must have an age too!".format(username2))

            # If second player's age is 10 or more then start this game mode.
            if age2 >= 10:
                # This while loop is for play again option.
                while True:
                    print("\nGame Started:")
                    attemptCount = 1  # Initial attempt.
                    # Try and exception repetition/check for first player input.
                    while True:
                        try:
                            usr_answer = int(input("->> {0} (attempt {1}): ".format(username, attemptCount)))
                            # Try and exception repetition/check for second player input.
                            while True:
                                try:
                                    usr2_answer = int(input("->> {0} (attempt {1}): ".format(username2, attemptCount)))
                                    # Once both input fields are valid, start the for loop.
                                    for attemptCount in range(attemptCount, attempts):
                                        if usr_answer == number == usr2_answer:
                                            print("\n** Hey, it's a DRAW, well done to both of you. "
                                                  "The answer is ({0}). **"
                                                  .format(number))
                                            break  # Exit for loop.

                                        if usr_answer == number:
                                            print("\n** {0} WINS, it is ({1}). You've guessed it in {2} attempt(s). **"
                                                  .format(username, number, attemptCount))
                                            break  # Exit for loop.

                                        if usr2_answer == number:
                                            print("\n** {0} WINS, it is ({1}). You've guessed it in {2} attempt(s). **"
                                                  .format(username2, number, attemptCount))
                                            break  # Exit for loop.

                                        if attemptCount == 2 and usr_answer != number != usr2_answer:
                                            print("\n** Oh it's the last chance to guess for both of you! **", end='\n')

                                        if attemptCount == 3 and usr_answer != number != computerGuess:
                                            print("\n** Sorry {0} and {1}, but you both lost! The number is ({2}). **"
                                                  .format(username, username2, number))
                                            break  # Exit for loop.

                                        else:
                                            attemptCount += 1
                                            # If player 1 answer is less than the number.
                                            if usr_answer < number:
                                                print("\n{0}, please guess higher than ({1})."
                                                      .format(username, usr_answer))
                                                usr_answer = int(input("->> {0}, (attempt {1}): "
                                                                       .format(username, attemptCount)))

                                            # If player 1 answer is greater than the number.
                                            else:
                                                print("\n{0}, please guess less than ({1})."
                                                      .format(username, usr_answer))
                                                usr_answer = int(input("->> {0}, (attempt {1}): "
                                                                       .format(username, attemptCount)))

                                            # If player 2 answer is less than the number.
                                            if usr2_answer < number:
                                                print("{0}, please guess higher than ({1})."
                                                      .format(username2, usr2_answer))
                                                usr2_answer = int(input("->> {0}, (attempt {1}): "
                                                                        .format(username2, attemptCount)))

                                            # If player 2 answer is greater than the number.
                                            else:
                                                print("{0}, please guess less than ({1})."
                                                      .format(username2, usr2_answer))
                                                usr2_answer = int(input("->> {0}, (attempt {1}): "
                                                                        .format(username2, attemptCount)))
                                # Player 2 answer (input) exception.
                                except ValueError:
                                    print("{0}, choose a number...".format(username2))
                                    continue
                                else:
                                    break
                        # Player 1 answer (input) exception.
                        except ValueError:
                            print("{0}, choose a number...".format(username))
                            continue
                        else:
                            break

                    while True:
                        # Option if two players wish to play again.
                        play_again = input("......................................\n"
                                           "->> Do you want to play again (Y/N)? ")
                        while True:
                            # Check if the input matches any of the list values.
                            if (play_again not in yes_list) and (play_again not in no_list):
                                print("Sorry, I didn't quite understand that.")
                                # The only way to prompt the question again as long as there is an input error
                                # is to duplicate the input prompt again in the loop.
                                # After many trials... this is what I have come up with.
                                play_again = input("......................................\n"
                                                   "->> Do you want to play again (Y/N)? ")
                            else:
                                break  # Breaks out of this while loop

                        if play_again in yes_list:
                            print("Cool, {0} and {1}, let's go...".format(username, username2))
                            # Choose a different number to guess if the player decides to play again.
                            number = random.randint(1, highest)
                            break  # Breaks out of second while loop.
                        else:
                            play_again = "no"
                            break  # Breaks out of second while loop.

                    if play_again in no_list:
                        print("Thank you for playing! Back to game mode...")
                        break  # Breaks out from the while loop following the age condition.
            # Age message if 2nd player is less than 10.
            else:
                change_mode = input("\nSorry, {0} is not old enough to play. "
                                    "Continue playing, {1}?\n"
                                    "Yes -- change game mode.\n"
                                    "No -- exit the game.\n".format(username2, username))
                if change_mode in no_list:
                    print(".......................................\n"
                          "Sorry about that {0}, hope to see you soon {1}!\n"
                          ".......................................".format(username2, username))
                    break  # Stop processing further, and terminate the game.
    # Age message if 1st player is less than 10.
    else:
        print("Sorry, you're not old enough for this game! Come back in {0} years.".format(10 - age))
