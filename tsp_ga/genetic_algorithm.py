import random
import numpy as np
from individual import Individual


class GeneticAlgorithm:
	def __init__(self, population_sz, individual_sz, max_iter, elitis_rate, mutation_rate, selection, crossover, mutation):
		self.population_sz = population_sz
		self.individual_sz = individual_sz
		self.max_iter = max_iter
		self.elitis_rate = elitis_rate
		self.mutation_rate = mutation_rate
		self.selection = selection
		self.crossover = crossover
		self.mutation = mutation

	@staticmethod
	def get_ranked_individuals(population):
		return sorted(population, key=lambda k: k.value)

	@staticmethod
	def update_values_of_fitness_after_mutation(population):
		for i in range(len(population)):
			population[i].value = population[i].calculate_value()

	def init_population(self):
		return [Individual(random.sample(range(1, self.individual_sz + 1), self.individual_sz))
		        for i in range(self.population_sz)]

	def elitis(self, old_pop, new_pop):
		num_of_olds = int(self.elitis_rate * self.population_sz)
		return old_pop[:num_of_olds] + new_pop[:(self.population_sz - num_of_olds)]

	def run(self):
		individuals = self.init_population()
		best_score = np.infty
		best_individual = None
		iteration = 0
		while iteration < self.max_iter:
			iteration += 1
			ranked_pop = self.get_ranked_individuals(individuals)
			pairs = self.selection(ranked_pop)
			children = self.crossover(pairs)
			children = self.mutation(children, self.mutation_rate)
			self.update_values_of_fitness_after_mutation(children)
			ranked_new = self.get_ranked_individuals(children)
			individuals = self.elitis(ranked_pop, ranked_new)
			curr_best = individuals[0]

			if curr_best.value < best_score:
				best_score = curr_best.value
				best_individual = curr_best

		return best_individual
