from utils import *
from Person import *


def initiate_simulation(N, immune_population, infected_population):
  population = []
  for i in range(N):
    # random_mask = random.randint(0,1)
    random_contagious_days = generate_contagious_days()
    random_contagiousness = generate_contagiousness()
    random_contagious_people = generate_contagious_people()
    random_mask = generate_mask()
    person = Person(immunity=1 if i < immune_population else 0,
                    contagious_days = 0 if i < N - infected_population else random_contagious_days,
                    contagiousness = 0 if i < N - infected_population else random_contagiousness,
                    contacted_people=random_contagious_people,
                    masks=0 if random_mask == 0 else 1,
                    daycount = 1 if not(i < N - infected_population-1) else 0)
    population.append(person)
  return population




# [  --- immune humans---, 
#  ---susceptible--- ,
#  ---infected---   ]



def run_day(population, number_of_days):
  number_of_sick_people=0
  N = len(population)
  for day in range(number_of_days):
    # count the number_of_sick_people 
    for i in range(N):
      if population[i].contagiousness > 0:
        number_of_sick_people += 1
    for person_index, person in enumerate(population):
      if person.contagiousness==0:
        pass
      else:
        person.daycount+=1
        if person.daycount > person.contagious_days:
          person.immunity = 1
          person.contagiousness = 0
          number_of_sick_people-=1
        
      # select contacted_people for the person 
        for i in range(person.contacted_people):
          random_inx = random.randint(0,N-1)        
          while random_inx == person_index:
            random_inx = random.randint(0,N-1)     
            
          if population[random_inx].contagiousness == 0 and  population[random_inx].immunity != 1:
            contagion_test = random.random()

            
            # lockdown code
            if number_of_days >=90:
              person.contagiousness = np.random.normal(0.1, 0.15, 1)
              if person.contagiousness<=0:
                person.contagiousness = 0
          # end lockdown code
            if contagion_test > person.contagiousness:
              pass
            else:
              population[random_inx].contagiousness = generate_contagiousness()
              population[random_inx].contagious_days = generate_contagious_days()
              number_of_sick_people+=1
          else:
            pass
  return population, number_of_sick_people

