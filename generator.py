import random


chars = ['0', '1']
number_of_chars = 8


def generate_string():
    string = ""
    for i in range(0, number_of_chars):
        random_no = random.randint(0, 1)
        string += chars[random_no]
    return string


def generate_number_of_turns(mini, maxi):
    return random.randint(mini, maxi)
