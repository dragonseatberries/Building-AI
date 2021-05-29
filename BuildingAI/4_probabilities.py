# exploring the use of probabilities
import random


def main():
    favorite = "none"
    prob = random.random()
    if prob < 0.2:
        favorite = "cats"
        if prob < 0.1:
            favorite = "bats"
    else:
        favorite = "dogs"

    print("I love " + favorite)


main()
