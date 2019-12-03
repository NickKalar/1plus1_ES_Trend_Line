import numpy
import csv
import random

data = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)


def mutate(parent):
    child = []
    for i in parent:
        child.append(i + numpy.random.normal(0.0, 1.0))
    return child


def fitness(array):
    sse = 0
    for row in data:
        x = float(row[0])
        yd = float(row[1])
        y = array[0] * pow(x, 3) + array[1] * pow(x, 2) + array[2] * x + array[3]
        sse += pow((yd - y), 2)
    return sse


def main():
    pop = []
    for i in range(4):
        pop.append(random.uniform(-20.0, 20.0))
    print(f"Starting Values: {pop}")
    for i in range(100):
        newPop = mutate(pop)
        newPopFitness = fitness(newPop)
        popFitness = fitness(pop)
        if newPopFitness < popFitness:
            pop = newPop
            popFitness = newPopFitness
        print(f"Iteration {i+1}: Values {pop}, Fitness {popFitness}")
    print(f"Ending Values: {pop}")

main()
