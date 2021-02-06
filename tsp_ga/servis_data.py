def get_data_from_file(f_name):
	with open(f_name, "r") as f:
		nodes = {}
		line = f.readline()
		while line:
			id_num, x, y = line.split()
			nodes[int(id_num)] = [float(x), float(y)]
			line = f.readline()
		return nodes


def write_result_to_file(f_name, result):
	with open(f_name, "w") as f:
		f.write(str(result.value) + '\n')
		f.write("______________________________________________________\n")
		f.write("Solution to TSP problem (visit cities in this order)\n"
		        "you can find cities ids and coordinates in data_tsp.txt\n"
		        "=======================================================\n"
		        "Distance calculated...{} km\n".format(result.value))
		f.write("=======================================================\n")
		for gen in result.genes:
			f.write(str(gen) + '\n')

	__check_writing_current_as_best(f_name, result)


def __check_writing_current_as_best(f_name, result):
	with open(__BEST_RESULT_FILE, "r+") as f:
		best = float(f.readline().strip())
		if result.value < best:
			f.seek(0)
			fread = open(f_name, "r")
			line = fread.readline()
			while line:
				f.write(line)
				line = fread.readline()
			fread.close()


# dictionary of cities, class Individual gets its fitness from NODES
NODES = None

__DATA_FILE = "data_tsp.txt"
__CURR_RESULT_FILE = "tsp_curent_result.txt"
__BEST_RESULT_FILE = "tsp_best_result.txt"
