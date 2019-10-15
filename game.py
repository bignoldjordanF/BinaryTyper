#!/usr/bin/python3

import generator
import time
import re


running = False


def intro():
    print("Game Loaded: 100%")
    print("")
    print("You must replicate the binary strings on screen: ")
    print("You can type quit to quit at any time.")
    print("")
    input("Press any key to begin:")


def start_game():
    global running
    running = True
    intro()


def end_game():
    global running
    running = False


def game_running():
    return running


def score_replica(original, replica, seconds_taken):
    correct = 0

    count = 0
    for ch in replica:
        if ch == original[count]:
            correct += 1
        count += 1

    perc = (correct / len(original)) * 100
    score = perc

    if seconds_taken <= 2.5:
        score *= 1
        print("Perfect speed!")
    elif seconds_taken <= 4:
        score *= 0.75
        print("Good speed!")
    elif seconds_taken <= 6:
        score *= 0.5
        print("Type quicker!")
    elif seconds_taken <= 7:
        score *= 0.25
        print("Too slow.")
    else:
        print("Far too slow.")
        score *= 0.00

    return round(score)


def input_valid(original, replica):

    if replica.lower() == "quit":
        end_game()
        return True

    regex = generator.get_regex()

    if not re.match(regex, replica):
        return False

    return True


def get_input(original):
    replica = input("> ")

    while not input_valid(original, replica):
        print("You can only enter 0 and 1s.")
        replica = input("> ")

    if replica == "quit":
        return replica

    # Too many characters
    if len(replica) > len(original):
        difference_in_length = len(replica) - len(original)

        if difference_in_length > len(original):
            difference_in_length = 8

        replica = replica[0:len(original)-difference_in_length]

        for i in range(0, difference_in_length):
            replica += "~"

        print("Too many characters! You have been penalised.")

    # Not enough characters
    if len(replica) < len(original):

        diff_in_length = len(original) - len(replica)

        for i in range(0, diff_in_length):
            replica += "~"

        print("Not enough characters! You have been penalised.")

    return replica


def calculate_time(millis1, millis2):
    return (millis2 - millis1) / 1000  # to seconds


def main(charz, number_of_charz):

    generator.set_values(charz, number_of_charz)

    start_game()

    overall_score = 0
    game_score = 0
    turns_so_far = 0

    max_turns = generator.generate_number_of_turns(6, 10)

    while game_running():

        curr_time_millis = int(round(time.time() * 1000))

        original = generator.generate_string()
        print("Type quit to exit at any time.")
        print("Quick! Type " + original + ": ")

        replica = get_input(original)

        if replica == "quit":
            break

        new_time_millis = int(round(time.time() * 1000))

        seconds_taken = calculate_time(curr_time_millis, new_time_millis)

        print("")
        score = score_replica(original, replica, seconds_taken)
        score_string = str(score)

        if score <= 30:
            print("Score: " + score_string + ". Abysmal attempt! You are losing time.")

        elif 30 < score < 60:
            print("Score: " + score_string + ". You can do better than that!!")

        elif 60 <= score <= 80:
            print("Score: " + score_string + ". Nice! Just concentrate a bit more!")

        else:
            print("Score: " + score_string + ". Well done! We can push the enemy back.")

        game_score += score
        turns_so_far += 1
        overall_score = game_score / turns_so_far

        if turns_so_far == max_turns:
            end_game()
            print("")
            print("You have matched all the binary strings.")

        print("")

    print("Thank you for matching the binary strings.")
    print("Your overall score was: " + str(round(overall_score)) + "/100!")
    print("Goodbye.")


main(["j", "a", "$"], 8)
