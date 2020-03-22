import numpy as np
import random
import string


class Member:

    MUTATION_PROB = 0.3

    def __init__(self, string):
        self.genes = string;
    # end __init__

    def reproduce(self, otherMember):
        length = len(self.genes)
        position = random.randrange(length)

        childOne = Member(self.genes[:-position] + otherMember.genes[:position])
        childTwo = Member(otherMember.genes[:-position] + self.genes[:position])

        finalList = [childOne, childTwo]
        return finalList

    def mutate(self):
        prob = random.uniform(0, 1)
        if prob <= self.MUTATION_PROB:
            length = len(self.genes)
            position = random.randrange(length);
            self.genes = self.genes[:position-1] + random.choice(string.ascii_lowercase) + self.genes[position:]
