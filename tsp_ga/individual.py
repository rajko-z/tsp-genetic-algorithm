import numpy as np
import servis_data

class Individual:
	def __init__(self, genes):
		self.genes = genes
		self.value = self.calculate_value()

	@staticmethod
	def _get_distance_between_to_nodes(node1_xy, node2_xy):
		return np.sqrt((node1_xy[0] - node2_xy[0])**2 + (node1_xy[1] - node2_xy[1])**2)

	def calculate_value(self):
		ret_val = 0
		for i in range(len(self.genes) - 1):
			node1_xy = servis_data.NODES[self.genes[i]]
			node2_xy = servis_data.NODES[self.genes[i + 1]]
			ret_val += self._get_distance_between_to_nodes(node1_xy, node2_xy)

		ret_val += self._get_distance_between_to_nodes(servis_data.NODES[self.genes[0]],
		                                               servis_data.NODES[self.genes[len(self.genes) - 1]])
		return ret_val
