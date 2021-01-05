#!/usr/bin/python3

# This script generates a string based on the chars defined in the main file.

import random


# default values
chars = ['0', '1']
number_of_chars = 8


# Set the values, i.e., change from the default values
def set_values(charz, number_of_charz):
    global chars
    global number_of_chars
    chars = charz
    number_of_chars = number_of_charz


# Returns the regex for this chars used in game
def get_regex():
    regex = "["
    for char in chars:
        regex += char
    regex += "]+"
    return regex


# Generate a random string from the chars of length number_of_chars
def generate_string():
    string = ""
    for i in range(0, number_of_chars):
        random_no = random.randint(0, len(chars)-1)
        string += chars[random_no]
    return string


# Decide a random number of turns in *this* game, given params as limits
def generate_number_of_turns(mini, maxi):
    return random.randint(mini, maxi)
