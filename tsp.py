import sys
import random
from makeTest import cities_costs
from math import perm


def generateParent(parent: list, start):
    child = parent.copy()
    random.shuffle(child)
    return start+child+start

def mutation(child):
    point1, point2 = sorted(random.sample(range(1,len(child)-1),2))
    child[point1], child[point2] = child[point2], child[point1]

def crossover(parent1, parent2, start):
    ln = len(parent1)
    point1, point2 = sorted(random.sample(range(1,ln-1),2))
    child1 = [-1]* ln
    child2 = [-1]* ln
    child1[0], child1[-1] = *start, *start
    child2[0], child2[-1] = *start, *start
    child1[point1 : point2] = parent2[point1: point2]
    child2[point1 : point2] = parent1[point1: point2]
    eq1 = []
    eq2 = []
    for i in range(1,ln-1):
        if child1[i] == -1:
            if parent1[i] in child1:
                if parent2[i] not in child1:
                    child1[i] = parent2[i]
                else:
                    eq1.append(i)
            else:
                child1[i] = parent1[i]
        if child2[i] == -1:
            if parent2[i] in child2:
                if parent1[i] not in child2:
                    child2[i] = parent1[i]
                else:
                    eq2.append(i)
            else:
                child2[i] = parent2[i]

    diff1 = list(set(parent1).difference(set(child1)))
    diff2 = list(set(parent2).difference(set(child2)))
    while eq1:
        child1[eq1.pop()] = diff1.pop()
    while eq2:
        child2[eq2.pop()] = diff2.pop()
    return child1, child2

def generatePopuation(Cities, start):
    population = []
    for i in range(min(perm(len(Cities)), 10)):
        parent = generateParent(Cities, start)
        while parent in population:
            parent = generateParent(Cities,start)
        population.append(parent)
    return population

def fitness(child):
    cost = 0
    for i in range(1,len(child)):
        try:
            cost += cities_costs[f'{child[i]}-{child[i-1]}']
        except:
            cost += cities_costs[f'{child[i-1]}-{child[i]}']
    return cost 

def main_tsp(Cities, start):
    if not cities_costs:
        print('You should add Costs.xlsx file that have form, to costs')
        quit()
    if start in Cities:
        Cities.remove(start)
    start = [start]
    mutation_rate = 0.2
    population = [[i,fitness(i)] for i in generatePopuation(Cities, start)]
    population.sort(key=lambda x: x[1])
    iterations = 200
    for iteration in range(iterations):
        parent1, fit1 = population[0]
        parent2, fit2 = population[random.randint(1,len(population)-1)]
        child1, child2 = crossover(parent1, parent2, start)
        mutation_ok = random.random()
        if mutation_ok <= mutation_rate:
            mutation(child1)
            mutation(child2)
        if child1 not in population:
            population.append([child1, fitness(child1)])
        if child2 not in population:
            population.append([child2, fitness(child2)])
        population.sort(key=lambda x: x[1])
        population = population[:len(population)]

    
    #          road               cost
    return population[0][0], population[0][1]