import numpy as np
import random


def generate_contagiousness():
  return np.random.normal(0.4, 0.2, 1)


def generate_contagious_days():
  return np.random.normal(5, 2, 1)


def generate_contagious_people():
  return int(np.round(np.random.normal(5, 2, 1), 0))


def generate_mask():
  return random.randint(0,1)
