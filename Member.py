import numpy as np
import random
import string


class Member:

    MUTATION_PROB = 0.3

    def __init__(self, genes):
        self.genes = genes;
        self.rawFitness = 0
        self.scaleFitness = 0
        self.normFitness = 0
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

    def calculateRawFitness(self, objective):
        length = len(self.genes)
        difLetters = sum(self.genes[i] != objective[i] for i in range(length))
        self.rawFitness = difLetters/length

    def calculateScaleFitness(self):
        self.scaleFitness = 2**self.rawFitness

    def calculateNormFitness(self, totalSum):
        self.normFitness = self.scaleFitness/totalSum

    def updateFitnesses(self, objective):
        self.calculateRawFitness(objective)
        self.calculateScaleFitness()

