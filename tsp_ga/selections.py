import random

def rulet_selection(population):
	pairs = []
	for i in range(0, len(population), 2):
		indexes = [(i+1) * random.random() for i in range(len(population))]
		ranked = sorted(list(zip(indexes, population)), key=lambda c: c[0])
		pairs.append([ranked[0][1], ranked[1][1]])
	return pairs
