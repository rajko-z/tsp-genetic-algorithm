import random
from individual import Individual

def __create_child(r1, r2, parent1, parent2, size):
	child1_base = parent1[r1:r2]
	all_cycle_parent2 = parent2[r2:] + parent2[:r2]
	valid_cycle_parent2 = [i for i in all_cycle_parent2 if i not in child1_base]
	child1 = valid_cycle_parent2[size - r2:] + child1_base + valid_cycle_parent2[:size - r2]
	return Individual(child1)


# Order Crossover Operator
def ox(pairs):
	size = len(pairs[0][0].genes)
	children = []
	for pair in pairs:
		r1 = random.randrange(1, size - 1)
		r2 = random.randrange(1, size - 1)
		r1 = min(r1, r2)
		r2 = max(r1, r2)
		parent1 = pair[0].genes
		parent2 = pair[1].genes
		children.append(__create_child(r1, r2, parent1, parent2, size))
		children.append(__create_child(r1, r2, parent2, parent1, size))

	return children

