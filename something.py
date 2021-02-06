import random as r
import time

start = time.time()

# ------------- Parser -------------
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

r.seed()
outputList = []
assignments = {}

# ------------- Simple Approach -------------
remPizzas = []
for i in range(0, len(pizzas)):
    remPizzas.append(i)

pizzaCounter = 0
for i in range(int(numOf2)):
    if len(remPizzas) >= 2:
        outputList.append([2, remPizzas.pop(0), remPizzas.pop(0)])
        pizzaCounter += 1

for i in range(int(numOf3)):
    if len(remPizzas) >= 3:
        outputList.append([3, remPizzas.pop(0), remPizzas.pop(0), remPizzas.pop(0)])
        pizzaCounter += 1

for i in range(int(numOf4)):
    if len(remPizzas) >= 4:
        outputList.append([4, remPizzas.pop(0), remPizzas.pop(0), remPizzas.pop(0), remPizzas.pop(0)])
        pizzaCounter += 1

print("Number of 2 people teams: {}".format(numOf2))
print("Size of assignments: {}".format(str(len(assignments))))

# ------------- Stochastic Approach -------------
def worth(t):
    uniqueValues = 0
    if t[0] == 2:
        uniqueValues = pizzas[t[1]] | pizzas[t[2]]
    if t[0] == 3:
        uniqueValues = pizzas[t[1]] | pizzas[t[2]] | pizzas[t[3]]
    if t[0] == 4:
        uniqueValues = pizzas[t[1]] | pizzas[t[2]] | pizzas[t[3]] | pizzas[t[4]]
    
    score = len(uniqueValues) ** 2
    # print("Score: {}".format(score))
    return score

for i in range(5000000):
    # Get random team value
    x1 = r.randint(1, len(outputList) - 1)
    x2 = r.randint(1, len(outputList) - 1)

    # Get random pizza in of the team
    y1 = r.randint(1, len(outputList[x1]) - 1)
    y2 = r.randint(1, len(outputList[x2]) - 1)

    # Find old score of both teams
    worth(outputList[x1])
    worth(outputList[x2])
    # print("TOTAL SCORE BEFORE: {}".format(worth(outputList[x1]) + worth(outputList[x2])))
    scoreBefore = worth(outputList[x1]) + worth(outputList[x2])

    outputList[x1][y1], outputList[x2][y2] = outputList[x2][y2], outputList[x1][y1]
    # print("TOTAL SCORE AFTER: {}".format(worth(outputList[x1]) + worth(outputList[x2])))
    scoreAfter = worth(outputList[x1]) + worth(outputList[x2])

    if scoreAfter < scoreBefore:
        outputList[x1][y1], outputList[x2][y2] = outputList[x2][y2], outputList[x1][y1]


# ------------- Output -------------
path = "outputc.txt"
output = open(path, "w")
output.write(str(pizzaCounter) + "\n")
for x in outputList:
    if x[0] == 2:
        output.write("{} {} {}\n".format(str(x[0]), str(x[1]), str(x[2])))
    if x[0] == 3:
        output.write("{} {} {} {}\n".format(str(x[0]), str(x[1]), str(x[2]), str(x[3])))
    if x[0] == 4:
        output.write("{} {} {} {} {}\n".format(str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4])))

# ------------- Time -------------
end = time.time()
print("Execution time: {}".format(end - start))
print(end - start)