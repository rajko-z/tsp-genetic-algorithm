# Travel salesman problem with genetic algorithm
Implementation of genetic algorithm to solve the instance of [travel salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) Berlin52.

## About problem
Task:  "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" . In short we have to find the [Hamiltonian circuit](https://en.wikipedia.org/wiki/Hamiltonian_path) in undirected graph.
Tsp is NP-hard problem, so there exist some nondeterministic solutions. This project tries to give the bast aproximation using [genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm). There are 52 cities in **data_tsp.txt** with their coordinates

## Genetic algorithm
### Fitness function
Tsp is minimization problem because we are searcing for smallest distance. We can write fitness function like this:
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
![first eqation](https://latex.codecogs.com/gif.latex?%5C%5BI_d%3D%5Csum%5E%7Bn-1%7D_%7Bi%3D1%7D%7BD%7D%5Cleft%28v_1%2Cv_%7B1&plus;i%7D%5Cright%29&plus;D%5Cleft%28v_%7Bn%5C%20%7D%2Cv_1%5Cright%29%5D%5C)

where D is the function of distance between to vertices, calculated with this formula:
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
![second_equation](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B120%7D%20%5C%5BD%5Cleft%28n_i%2C%5C%20%5C%20n_j%5Cright%29%3D%5Csqrt%7B%7B%5Cleft%28x_i-x_j%5Cright%29%7D%5E2&plus;%7B%5Cleft%28y_i-y_j%5Cright%29%7D%5E2%7D%5C%5D)

### Initialization of population
At the beginning, we assign a certain number of population size, and randomly select strings of different numbers that go from 1 to n. Once we have made the initial population, we calculate how much each individual is worth according to the fitness function

### Parent pair selection
Parents are selected by roulette selection with rank. To avoid problems such as superunits, we will rank with numbers from 1 to n the entire generation we observe, according to the calculated fitness function. Since we are looking for a minimum, the best unit will have a value of 1 and the worst a value of n. We go through n / 2 iterations and choose two parents each. In order not to choose the same two parents every time, we introduce a random factor, which we multiply by the calculated rank and get the final distribution of the selected individuals.

### Crossing
There are various ways we can cross our individuals, I opted for the **order crossover operator** (or just OX in the literature). <br />
First we choose random boundaries and cut both parents along those boundaries, then we put what is left between the boundaries in order, in the first and second child. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
P1 = (1 2 4 | 5 3 8 | 7 6)    -->    C1 = (* * * | 5 3 8| * *) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
P2 = (3 2 5 | 8 1 4 | 6 7)    -->    C2 = (* * * | 8 1 4| * *) <br />
We fill in the rest of the field of the first child by taking the whole cycle of the second parent, moving from the second intersection point, and removing the elements that are already in the first child.
The cycle of the second parent is 6 7 3 2 5 8 1 4, ie when the elements that are already in the first child are removed, we get the cycle 6 7 2 1 4. <br />
We are now filling in the rest of the first child, starting from the second intersection point. So we get the following form: C1 = (2 1 4 | 5 3 8 | 6 7). The procedure is identical and in the opposite case, for the second child we get the following form: C2 = (2 5 3 | 8 1 4 | 7 6) because the cycle of the first parent is 7 6 2 5 3.

### Mutation
Another crucial factor in a genetic algorithm is the selection of the appropriate mutation. I tried several mutation methods, but **reverse sequence mutation (rms)** proved to be the best. We select two random numbers and then reverse all numbers within that range. For example: <br />
Let P1 be the observed unit, and let us randomly choose two numbers going from 1 to n - 1 to obtain the following limits <br />
P1 = (1 2 4 | 5 3 8 | 7 6)
the next step is to invert all the numbers in that limit and thus we obtain a mutated unit <br /> P1 = (1 2 4 | 8 3 5 | 7 6)

### Elitism
I have decided to support the possibility for a certain part of the individuals to continue living in the next generation, and not to completely change the generation with a new one.

### Testing and program structure
The algorithm was tested for the TSP instance of the Berlin52 problem for which the shortest solution is known to be **7544.3659**. The modules **crossovers.py**, **selections.py** and **mutations.py** contain the main functions of the algorithm, as well as the ability to add new ones. For example, there are a number of different mutation modes in the mutations.py module, of which, as I said earlier, reverse sequence mutation gives the best result in combination with the order crossover operator.
The individual itself is represented by the class **Individual**, which contains the path and value of the fitness function. <br />
All the necessary methods are in the **GeneticAlgorithm** class, where when calling the algorithm we can pass all the necessary parameters as well as the functions we want to use for the most important operations such as selection, combination and mutation.

### Parametars
An appropriate balance needs to be found between the execution speed of the algorithm and the accuracy of the results. In our example, the algorithm behaves best for the following parameters: <br />
- mutation_rate = 0.3 <br />
- elitis_rate = 0.1 <br />

where the number of maximum iterations is 500 and the number of units is 200 (for some larger numbers the algorithm does not give drastically better solutions, and the execution becomes longer, so I limited myself to these values) <br />
At program startup (**main.py**) the result of one execution is recorded in **tsp_current_result.txt** and if that result is better than the best result ever measured in previous runs, the content of the best one is automatically changed (**tsp_best_result.txt**). The following is a display of the results of running the algorithm 100 times. Each execution is started with 500 iterations and the above parameters. 








