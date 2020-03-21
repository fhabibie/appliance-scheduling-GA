import pandas as pd
import numpy as np
import random
import os
import datetime

def parse_date(date):
    return datetime.datetime.strptime(date, '%I:%M:%S %p')

def time_index(time):
    init_time = parse_date('12:00:00 AM')
    deltatime = time - init_time
    return int(deltatime.total_seconds()/3600*2)

class Chromosome:
    def __init__(self, gene, costs):
        self._gene = gene
        self._fitness = self.fitness_function()
        self._costs = costs
        
    @property
    def gene(self):
        return self._gene
    @property
    def costs(self):
        return self._costs
    @property
    def fitness(self):
        return self._fitness

    def mutation(self):
        return Chromosome(self._gene)

    def crossover(self):
        return Chromosome(self._gene)

    def is_feasible(self):
        return 'boolean value'

    def fitness_function(self):
        tmp=0.0
        for i in range(len(self._gene)):
            tmp += np.sum(self._gene[i])
        return tmp


class Population():
    def __init__(self, appliances_df, size=10, mutation_rate=0.05, crossover_rate=0.8):
        self.size = size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.appliances_df = appliances_df
        
    def generate_random_individual(self):              
#       Create zeros element array with size = number of appliances * 48 (time sch)
        app_sch = np.zeros((len(self.appliances_df), 48), int)
        
        for i in range(0, len(app_sch)):
            max_duration = int(self.appliances_df.iloc[i]['duration']*2)
            start_element = time_index(self.appliances_df.iloc[i]['start'])
            end_element = time_index(self.appliances_df.iloc[i]['end'])
            for j in range(0, max_duration):
                rand_index = random.randrange(start_element, end_element+1)
                app_sch[i, rand_index] = 1
        return Chromosome(app_sch, self.appliances_df['costs'].to_numpy())
        
    def generate_population(self):
        pop_lists = []
        for i in range(0, self.size):
            pop_lists.append(self.generate_random_individual())
  
        return pop_lists

    def roullete_wheel(self):
        return 'tuple of chromosome'

    def parent_selection(self):
        return 'population'

#%%
if __name__ == "__main__":
    generation_size = 100
    
    
    appliances_df = pd.read_csv('sample-data.csv', parse_dates=['start', 'end'], date_parser=parse_date)
    
    pop = Population(appliances_df)
    first_pop = pop.generate_population()
    print('Number of population', len(first_pop))
    