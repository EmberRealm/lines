import random

def read_random_line(filename):
    lines = open(filename).read().splitlines()
    return random.choice(lines)

def communicate_with_other_part(other_part):
    line = read_random_line('myfile.txt')
    other_part.process_line(line)
