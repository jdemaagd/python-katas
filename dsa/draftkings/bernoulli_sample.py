import random


def bernoulli_sample(p):
    return 1 if random.random() < p else 0


prob = 0.7
print(bernoulli_sample(prob))  # Output: 1 or 0 with probability 0.7 or 0.3 respectively
