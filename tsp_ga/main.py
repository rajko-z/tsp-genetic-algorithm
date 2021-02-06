import servis_data
import selections
import crossovers
import mutations
from genetic_algorithm import GeneticAlgorithm


def prompt(best):
	print("==========TSP============")
	print("Best solution (distance) ->> ", best.value)
	print("Order of visiting : ")
	for i in range(len(best.genes)):
		if i == len(best.genes) - 1:
			print(best.genes[i])
		else:
			print(best.genes[i], end=' ==>')
	print("========================")


def main():
	servis_data.NODES = servis_data.get_data_from_file(servis_data.__DATA_FILE)
	in_sz = len(servis_data.NODES)

	GA = GeneticAlgorithm(population_sz=200,
	                      individual_sz=in_sz,
	                      max_iter=500,
	                      elitis_rate=0.1,
	                      mutation_rate=0.3,
	                      selection=selections.rulet_selection,
	                      crossover=crossovers.ox,
	                      mutation=mutations.rsm)

	best = GA.run()
	prompt(best)
	servis_data.write_result_to_file(servis_data.__CURR_RESULT_FILE, best)


if __name__ == '__main__':
	main()