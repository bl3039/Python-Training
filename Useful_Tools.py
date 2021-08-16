
# This belongs to Lesson 28 Modules and Pip

import random

feet_in_mile = 5280
metres_in_kilometres = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)