# probabilities used in simulated annealing
import random
import numpy as np


def accept_prob(S_old, S_new, T):
    # acceptance probability in simulated annealing
    if S_new > S_old:
        return 1.0
    return np.exp(-(S_old - S_new)/T)


def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)
