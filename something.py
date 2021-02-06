# Parser
fp = open("./c_many_ingredients.in", "r")
firstLine = fp.readline()
numOfPizzas = firstLine.split(" ")[0]
numOf2 = firstLine.split(" ")[1]
numOf3 = firstLine.split(" ")[2]
numOf4 = firstLine.split(" ")[3]

pizzas = []
for line in fp.readlines():
    pizzas.append(set(line.replace("\n", "").split(" ")[1:]))

fp.close()

# ------------- Stochastic approach -------------
import random as r
import time

start = time.time()

r.seed()
checked = []
assignments = {}

# 2 teams
for i in range(0, int(numOf2)):
    firstIteration = True
    px = []
    py = []

    while firstIteration or (len(px.intersection(py)) <= 10):
        x = r.randint(0, len(pizzas) - 1)
        while x in checked:
            x = r.randint(0, len(pizzas) - 1)
        px = pizzas[x]

        y = r.randint(0, len(pizzas) - 1)
        while y in checked:
            y = r.randint(0, len(pizzas) - 1)
        py = pizzas[y]

    # print("{} => {}".format(str(x), str(y)))
    assignments[x] = y
    checked.append(x)
    checked.append(y)

print("Number of 2 people teams: {}".format(numOf2))
print("Size of assignments: {}".format(str(len(assignments))))

end = time.time()
print("Execution time: {}".format(end - start))
print(end - start)
