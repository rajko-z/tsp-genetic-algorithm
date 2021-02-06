import random


# Reverse sequence mutation
def rsm(population, mutation_rate):
	mutated = []
	size = len(population[0].genes)
	for ind in population:
		if random.random() < mutation_rate:
			left = random.randrange(0, size)
			right = random.randrange(0, size)
			left = min(left, right)
			right = max(left, right)
			while left < right:
				ind.genes[left], ind.genes[right] = ind.genes[right], ind.genes[left]
				left += 1
				right -= 1
		mutated.append(ind)
	return mutated


# Partial shuffle mutation
def psm(population, mutation_rate):
	mutated = []
	size = len(population[0].genes)
	for ind in population:
		if random.random() < mutation_rate:
			for i in range(len(ind.genes)):
				if random.random() < mutation_rate:
					r = random.randrange(0, size)
					ind.genes[i], ind.genes[r] = ind.genes[r], ind.genes[i]
		mutated.append(ind)
	return mutated


# The  Hybridizing  PSM  and  RSM
def hybrid_rsm_psm(population, mutation_rate):
	mutated = []
	size = len(population[0].genes)
	for ind in population:
		if random.random() < mutation_rate:
			left = random.randrange(0, size)
			right = random.randrange(0, size)
			left = min(left, right)
			right = max(left, right)
			while left < right:
				ind.genes[left], ind.genes[right] = ind.genes[right], ind.genes[left]
				if random.random() < mutation_rate:
					r = random.randrange(0, size)
					ind.genes[left], ind.genes[r] = ind.genes[r], ind.genes[left]
				left += 1
				right -= 1
		mutated.append(ind)
	return mutated

# Displacement Mutation (DM)
def __dm(individua):
	size = len(individua.genes)
	left = random.randrange(0, size)
	right = random.randrange(0, size)
	left = min(left, right)
	right = max(left, right)
	subgenes = individua.genes[left:right]
	individua.genes = individua.genes[:left] + individua.genes[right:]
	random_spot = random.randrange(0, len(individua.genes))
	individua.genes = individua.genes[:random_spot] + subgenes + individua.genes[random_spot:]
	return individua

def dm(population, mutation_rate):
	mutated = []
	for ind in population:
		if random.random() < mutation_rate:
			mutated.append(__dm(ind))
		else:
			mutated.append(ind)
	return mutated


# Insertion Mutation (ISM)
def __ism(individua):
	size = len(individua.genes)
	left = random.randrange(0, size)
	right = random.randrange(0, size)
	individua.genes[left], individua.genes[right] = individua.genes[right], individua.genes[left]
	return individua

def ism(population, mutation_rate):
	mutated = []
	for ind in population:
		if random.random() < mutation_rate:
			mutated.append(__ism(ind))
		else:
			mutated.append(ind)
	return mutated

# Hybrid ism and dm
def hybrid_dm_ism(population, mutation_rate):
	mutated = []
	for ind in population:
		if random.random() < mutation_rate:
			if random.random() < 0.5:
				mutated.append(__dm(ind))
			else:
				mutated.append(__ism(ind))
		else:
			mutated.append(ind)
	return mutated

