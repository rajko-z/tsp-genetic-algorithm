import matplotlib.pyplot as plt


f = open("just_distances.txt", "r")
data = {}
br = 1
best = 1000000000
best_index = 0
line = f.readline()
while line:
	val = float(line.strip())
	data[br] = val
	if val < best:
		best = val
		best_index = br 
	line = f.readline()
	br += 1
f.close()

# =======================
avg = sum(data.values()) / len(data)
tsp_solution = 7544.3659
# ========================

names = list(data.keys())
values = list(data.values())

plt.bar(names, values, color=(0.2, 0.4, 0.6, 0.6))

x = [i for i in range(1, len(data) + 1)]
y = [tsp_solution for i in range(len(data))]
plt.plot(x, y, 'green', label="Exact solution: {}".format(tsp_solution))

x = [i for i in range(1, len(data) + 1)]
y = [avg for i in range(len(data))]
plt.plot(x, y, 'red', label="Average: {}".format(avg))

plt.scatter(best_index, int(best), c='black', linewidths=2, label="Best: {}".format(best))

print("odstupanje proseka od resenja: ", (avg - tsp_solution) / tsp_solution * 100 )
print("odsutupanje najboljeg od resenja: ", (best - tsp_solution) / tsp_solution * 100)

plt.legend(loc="lower right")
plt.show()



