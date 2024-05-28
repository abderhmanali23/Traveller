import sys
import random
import matplotlib.pyplot as plt
from makeTest import cities_costs


def generateParent(n_component, Cities):
    return random.sample(Cities,n_component)

def min_cost(n):
    lst = sorted(list(cities_costs.values()))
    return sum(lst[:n]+[lst[0]])

def crossover(parent1, parent2):
    ln = len(parent1)
    point1, point2 = sorted(random.sample(range(1,ln),2))
    child1 = [-1]* ln
    child2 = [-1]* ln
    child1[point1 : point2] = parent2[point1: point2]
    child2[point1 : point2] = parent1[point1: point2]
    eq1 = []
    eq2 = []
    for i in range(ln):
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

def mutation(child,Cities):
    diff = list(set(Cities).difference(set(child)))
    if len(diff):
        rand = random.choice(diff)
        ind = random.randint(0,len(child)-1)
        child[ind] = rand

def fitness(child):
    cost = 0
    for i in range(1,len(child)):
        try:
            cost += cities_costs[f'{child[i]}-{child[i-1]}']
        except:
            cost += cities_costs[f'{child[i-1]}-{child[i]}']
    return cost 

def generatePopuation(n, Cities):
    population = []
    for i in range(15):
        parent = generateParent(n, Cities)
        while parent in population:
            parent = generateParent(n, Cities)
        population.append(parent)
    return population

def main_bestRoad(budget):
    Cities = ['Port Said', 'Sohag', 'Suez', 'Red Sea', 'Luxor', 'Beni Suef', 'Kafr El Sheikh', 'Dakahlia', 'Helwan', 'Aswan', 'Faiyum', 'Gharbia', 'South Sinai', 'Monufia', 'Matrouh', 'Qalyubia', 'Sharqia', 'Qena', 'Beheira', 'Alexandria', 'Damietta', 'Cairo', 'Giza', 'Asyut', 'North Sinai', 'New Valley', 'Ismailia', 'Minya']
    mutation_rate = 0.1
    n = 3
    result = []
    while min_cost(n) <= budget and n < len(Cities):     
        population = [[i, fitness(i+[i[0]])] for i in generatePopuation(n, Cities)]
        population.sort(key=lambda x:x[1])
        iterations = 500
        for iteration in range(iterations):
            parent1, fit1 = population[0]
            parent2, fit2 = population[random.randint(1,len(population)-1)]
            child1, child2 = crossover(parent1, parent2)
            mutation_ok = random.random()
            if mutation_ok <= mutation_rate:
                mutation(child1, Cities)
                mutation(child2, Cities)
            if child1 not in population:
                population.append([child1, fitness(child1+[child1[0]])])
            if child2 not in population:
                population.append([child2, fitness(child2+[child2[0]])])
            population.sort(key=lambda x: x[1])
            population = population[:len(population)]
        if population[0][1] <= budget:
            result.append([population[0][0]+[population[0][0][0]], population[0][1]])
        else:
            lst = sorted(list(cities_costs.items()),key= lambda x: x[1])[:n//2+1]
            distination= [i[0].split('-') for i in lst]
            final_distination = []
            for i in distination:
                for j in i:
                    final_distination.append(j)
            if n%2:
                final_distination.pop()
            else:
                final_distination.pop()
                final_distination.pop()
            final_distination = final_distination+[final_distination[0]]
            final_cost = min_cost(n)
            result.append([final_distination, final_cost])
        n += 1

    if n == 3:
        return 'There is no way with this budget'

    return result