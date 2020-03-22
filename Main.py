import string
import random
from Member import Member


def randomString(size):
    letters = string.ascii_letters + " "
    return ''.join(random.choice(letters) for i in range(size))


def initializePopulation(size, lenString, objString):
    pop = []
    for i in range(size):
        gen = randomString(lenString)
        m = Member(gen)
        m.updateFitnesses(objString)
        pop.append(m)
    return pop


def calculateTotalFitness(memPop):
    total = 0
    for m in memPop:
        total += m.scaleFitness
    return total


if __name__ == "__main__":

    objectiveString = "Me llamo Daniel"
    iterations = 10

    populationSize = 500
    sizeString = len(objectiveString)

    population = initializePopulation(populationSize, sizeString)

    totalFitness = calculateTotalFitness(population)

    for i in range(iterations):
        print("HAHAH")
