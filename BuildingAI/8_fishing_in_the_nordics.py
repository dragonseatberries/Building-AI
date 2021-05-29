# using bayes theorem and knowledge of conditional probabilities to solve probability problems
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

total_male_fishers = sum(male_fishers)
total_female_fishers = sum(female_fishers)


def guess(winner_gender):
    # decide whether we're looking at female fishers or male fishers
    if winner_gender == 'female':
        fishers = female_fishers
        total_fishers = total_female_fishers
    else:
        fishers = male_fishers
        total_fishers = total_male_fishers

    guess = None
    biggest = 0.0
    # loop through all countries and fishers and keep track of the biggest probability
    # brute forcing
    for country, fishers in zip(countries, fishers):
        prob = fishers/total_fishers * 100
        if prob > biggest:
            guess = country
            biggest = prob
    return (guess, biggest)


def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (
        country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (
        country, fraction))


main()
