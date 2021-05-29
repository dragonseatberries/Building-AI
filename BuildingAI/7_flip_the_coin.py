# using the monte carlo method in probability problems
# basically just generate a large batch of random data and count the occurences of what you are keeping track of to then find an approximate probability
import numpy as np


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], p=[1-p1, p1], size=9996)
    return seq


def count(seq):
    c = 0
    # insert code to return the number of occurrences of 11111 in the sequence
    for i in range(len(seq)):
        if seq[i:i+5].all():
            c += 1
    return c


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2/3))
