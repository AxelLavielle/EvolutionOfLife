import numpy as np
import random

#HyperParameters
keepSize = int(10) #How much population we keep from the last step
populationSize = int(100) #Size of our population
keepRatio = populationSize/keepSize #Ratio of staying population
mutationRate = 0.1 #Rate of the mutation
mapSize = int(250) #Size of the map
individualSize = int(10) #Size of the map
epoch = int(100) #Number of map iterations

#Game variables
map = None
population = None
fitness = np.zeros((1, populationSize))

def nextStep(iteration):
    global map
    global mapSize
    global individualSize

    newMap = np.zeros((mapSize,mapSize))
    for y in range(int(mapSize/2)-iteration-individualSize, int(mapSize/2)+iteration+individualSize):
        for x in range(mapSize):
            if (map[y][x] == 1):
                newMap[y-1][x-1] += 1
                newMap[y-1][x] += 1
                newMap[y-1][x+1] += 1
                newMap[y][x-1] += 1
                newMap[y][x+1] += 1
                newMap[y+1][x-1] += 1
                newMap[y+1][x] += 1
                newMap[y+1][x+1] += 1
    for y in range(mapSize):
        for x in range(mapSize):
            if (newMap[y][x] == 0 or newMap[y][x] > 3):
                map[y][x] = 0
            elif ((map[y][x] == 1 and (newMap[y][x] == 3 or newMap[y][x] == 2)) or
                (map[y][x] == 0 and newMap[y][x] == 3)):
                map[y][x] = 1
            else:
                map[y][x] = 0
    return (map)

def score():
    global mapSize

    fit = 0
    for y in range(mapSize):
        for x in range(mapSize):
            if (map[y][x] == 1):
                fit += 1
    return (fit)

def mutate():
    global populationSize
    global mutationRate
    global individualSize
    global population

    for i in range(populationSize * mutationRate):
        population[random.randint(0, populationSize)][random.randint(0, individualSize)][random.randint(0, individualSize)] = 1 - population[random.randint(0, populationSize)][random.randint(0, individualSize)][random.randint(0, individualSize)]

def evolve(elite):
    global population
    global keepRatio

    for i in range (0, populationSize):
        if (i % keepRatio == 0):
            population[i] = elite[i / keepRatio]
        else:
            population[i] = elite[i / keepRatio]

def select():
    global keepSize
    global keepRatio
    global populationSize
    global population
    global fitness

    elite = np.empty((1, keepSize))
    for i in range(0,populationSize,keepRatio):
        elite[i/keepRatio] = population[np.argmax(fitness[i:i + keepRatio])]
    return (elite)

def computeOneStep(individual):
    global map
    global mapSize
    global individualSize
    global epoch

    map = np.zeros((mapSize,mapSize))
    a = int(mapSize / 2 - individualSize / 2)
    for y in range(individualSize):
        for x in range(individualSize):
            map[a + y][a + x] = individual[y][x]
    for i in range(epoch):
        str = ""
        for y in range(individualSize):
            for x in range(individualSize):
                str += "%d"%map[a+y][a+x]
            str+="\n"
        print(str)
        map = nextStep(i)
    return (fitness)

def nextEpoch():
    global population
    global populationSize
    global individualSize

    if (population == None):
        population = np.empty((populationSize, individualSize, individualSize))
        for x in range(populationSize):
            population[x] = np.random.randint(0, 2, (individualSize, individualSize))
    else:
        elite = select()
        population = evolve(elite)
        population = mutate()
    for i in range(populationSize):
        fitness[i] = computeOneStep(population[i])

nextEpoch()