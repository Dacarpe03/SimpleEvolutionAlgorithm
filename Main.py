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
        newMember = Member(gen)
        newMember.updateFitnesses(objString)
        pop.append(newMember)
    return pop


def updFit(pop, objString):
    for m in pop:
        m.updateFitnesses(objString)
    return pop


def calculateTotalFitness(memPop):
    total = 0
    for m in memPop:
        total += m.scaleFitness
    return total


def initializeNormFitness(population, total):
    for m in population:
        m.calculateNormFitness(total)


if __name__ == "__main__":

    objectiveString = "Esta no es una frase larga"
    iterations = 10000

    populationSize = 250
    sizeString = len(objectiveString)

    population = initializePopulation(populationSize, sizeString, objectiveString)
    auxPop = []

    for i in range(iterations):

        population = updFit(population, objectiveString)
        totalFitness = calculateTotalFitness(population)
        initializeNormFitness(population, totalFitness)

        auxPop.clear()

        memberOne = population[0]
        memberTwo = population[1]

        while len(auxPop) < populationSize:
            for member in population:
                if member.normFitness > memberOne.normFitness:
                    memberOne = member
                    population.remove(member)
                elif member.normFitness > memberTwo.normFitness:
                    memberTwo = member
                    population.remove(member)

            children = memberOne.reproduce(memberTwo)
            auxPop.append(memberOne)
            auxPop = auxPop + children

        print("Best in iteration", i, ":", auxPop[0].genes)
        population = auxPop.copy()


    for member in population:
        if member.genes == objectiveString:
            print(member.genes)


