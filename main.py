from Person import *
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from utils import *
from pandemic_functions import *


def testing (N, immune_population, infected_population, number_of_days):
  population = initiate_simulation(N, immune_population, infected_population)
  population, number_of_sick_people  = run_day(population, number_of_days)
  contagious_list.append(number_of_sick_people)
  return population

N = 100000
immune_population = 0
infected_population = 1
number_of_days = 365

population, contagious_list = testing(N, immune_population, infected_population, number_of_days)

# print(population[1].contagiousness)

x = range(number_of_days)
y = contagious_list

plt.plot(x,y)
plt.savefig("picture.png")

