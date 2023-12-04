import numpy as np
import random

#assume: when you get sick, you have 0 contagiousness (you are home)
#assume: contact days = the days you interact with people bc you don't know you are sick
#assume: contacted people = people you interact with during one contact day


class Person:

  def __init__(self, immunity, contagious_days, contacted_people,
               contagiousness, masks, daycount):
    self.immunity = immunity  # am I immune?
   # self.infection = infection  # boolean (0 or 1), am I infected
    self.contagious_days = contagious_days  # integer; once I get infected, for how many days will I stay contagious

    self.contacted_people = contacted_people  # integer; how many people I come in contact with on a typical day

    self.masks = masks  # boolean, do I wear a mask

    self.contagiousness = contagiousness  # probability of infecting someone I come in contact with if I am infected

    if self.masks == 1:
      self.contagiousness = contagiousness * .5
    self.daycount = daycount

  # def contagiousness(self, contact_days, contact_people, masks):

  # def contagiousness(self, contacted_days, contacted_people, masks):
  #   #not in % bc on ave 1 spread to 2
  #   contacted_days = self.contacted_days
  #   contacted_people = self.contacted_people

  #   return float(out_contagiousness)
