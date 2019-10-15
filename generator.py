#!/usr/bin/python3

import random


# default values
chars = ['0', '1']
number_of_chars = 8


def set_values(charz, number_of_charz):
    global chars
    global number_of_chars
    chars = charz
    number_of_chars = number_of_charz


def get_regex():
    regex = "["
    for char in chars:
        regex += char
    regex += "]+"
    return regex


def generate_string():
    string = ""
    for i in range(0, number_of_chars):
        random_no = random.randint(0, len(chars)-1)
        string += chars[random_no]
    return string


def generate_number_of_turns(mini, maxi):
    return random.randint(mini, maxi)
