#!/usr/bin/python3
# A very simple game in Python to get the ball rolling again.

import generator
import time
import re


# Global Var(s)
# Is the game currently running?
running = False


def main(charz, number_of_charz):
    global running

    # Set the values being used for *this* game
    generator.set_values(charz, number_of_charz)

    # Start the game
    start_game()

    # These vars track the user progress through the game
    overall_score = 0
    game_score = 0
    turns_so_far = 0

    # Decide a random number of turns between limits [param1, param2]
    max_turns = generator.generate_number_of_turns(6, 10)

    # Game Loop
    # Do this while the game is still running (running = True)
    while running:

        # We're going to track the time, so store the current time in millis
        curr_time_millis = int(round(time.time() * 1000))

        # Now generate a random string to have the player replicate
        original = generator.generate_string()
        print("Type quit to exit at any time.")
        print("Quick! Type " + original + ": ")

        # Get the user copy of the string
        replica = get_input(original)

        # Get the time after the replica has been input
        new_time_millis = int(round(time.time() * 1000))

        # Calculate the number of seconds taken to complete the replica
        seconds_taken = (new_time_millis - curr_time_millis) / 1000

        print("")
        # Find the score of the attempt given the seconds taken
        score = score_replica(original, replica, seconds_taken)
        score_string = str(score)

        # Print (encouraging) messages based on score
        if score <= 30:
            print("Score: " + score_string + ". Aw man! You can do better than that!")

        elif 30 < score < 60:
            print("Score: " + score_string + ". Not bad! Work those fingers!")

        elif 60 <= score <= 80:
            print("Score: " + score_string + ". Nice! Just concentrate a bit more!")

        else:
            print("Score: " + score_string + ". Well done! Amazing effort.")

        # Add to the total game score this score
        game_score += score
        turns_so_far += 1  # Increment the turns so far
        overall_score = game_score / turns_so_far  # Calculate the overall score

        if turns_so_far == max_turns:
            running = False
            print("")
            print("You have matched all the binary strings.")

        print("")

    print("Thank you for matching the binary strings.")
    print("Your overall score was: " + str(round(overall_score)) + "/100!\n")
    end_game()


# Start The Game
def start_game():
    global running
    running = True  # The game is now running!
    intro()  # Show introduction


# Introductory Messages (Instructions)
def intro():
    print("You must replicate the binary strings on screen: ")
    print("You can type quit to quit at any time.")
    print("")
    input("Press any key to begin:")


# Get the player replica of the original string
# This function also influences score by comparing ...
    # the length of the input with the length of the original
def get_input(original):
    replica = input("> ")  # Get input

    if replica.lower() == "quit":
        end_game()

    # If the input is invalid ask for it again
    while not input_valid(original, replica):
        print("You can only enter 0 and 1s.")
        replica = input("> ")  # Enter the whole string again!

    diff_length = len(replica) - len(original)

    # Too many characters
    # Here, every excess character is penalised as a missed character.
    if diff_length > 0:

        # If the player typed over len(original)+len(original) characters
        if diff_length > len(original):
            diff_length = 8  # The max penalty is for 8 incorrect characters.

        # Shorten the replica as if the had missed diff_length characters
        replica = replica[0:len(original)-diff_length]

        # Replace those with a different char
        # [In retrospect: this is a big problem as this could be a char that the player needs to type]
        for i in range(0, diff_length):
            replica += "~"

        print("Too many characters! You have been penalised.")

    # Not enough characters
    elif diff_length < 0:

        # Follows the same logic as above, replacing missed characters with a different char
        # Take the absolute difference so we don't get a negative range
        for i in range(0, abs(diff_length)):
            replica += "~"

        print("Not enough characters! You have been penalised.")

    # Return the processed replica
    return replica


# Check that the input is valid
def input_valid(original, replica):

    # Quit the game if the player wishes to
    if replica.lower() == "quit":
        end_game()
        return True

    # Get the regex from generator script
    regex = generator.get_regex()

    # If it does not match the replica, the string is invalid.
    if not re.match(regex, replica):
        return False

    return True


# Score the replica in terms of seconds taken and accuracy
def score_replica(original, replica, seconds_taken):
    correct = 0  # Number of correct characters

    count = 0  # Number of chars iterated counter
    for ch in replica:
        if ch == original[count]:  # If char is the same as corresponding in original
            correct += 1  # It is correct
        count += 1

    # Calculate a percentage of accuracy
    perc = (correct / len(original)) * 100
    score = perc

    # The seconds_taken result in a score multiplier, affecting the result
    if seconds_taken <= 2.5:
        score *= 1  # E.g., the best time does not affect the accuracy store
        print("Perfect speed!")
    elif seconds_taken <= 4:
        score *= 0.75  # E.g., but this one reduces the % to three quarters its original
        print("Good speed!")
    elif seconds_taken <= 6:
        score *= 0.5
        print("Not a bad speed!")
    elif seconds_taken <= 7:
        score *= 0.25
        print("Type a little faster!")
    else:
        print("Too slow. I'm sure you can do better!")
        score *= 0.00  # E.g., and a really slow time results in 0 score.

    # We want to return an integer (whole) value, so use round()
    return round(score)


# End The Game
def end_game():
    print("Thank you for playing Binary Typer.")
    print("Goodbye.")
    exit(0)


# Run the game, in this case with chars 1 and 0, and each string of length 8.
main(["1", "0"], 8)
