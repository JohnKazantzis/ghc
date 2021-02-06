import random as r
import time

r.seed()

def parser():
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

    return numOfPizzas, numOf2, numOf3, numOf4, pizzas

def simpleApproach(pizzas, numOf2, numOf3, numOf4):
    # ------------- Simple Approach -------------
    outputList = []
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

    return outputList, pizzaCounter

# ------------- Stochastic Approach -------------
def score(t, pizzas):
    uniqueValues = 0
    if t[0] == 2:
        uniqueValues = pizzas[t[1]] | pizzas[t[2]]
    if t[0] == 3:
        uniqueValues = pizzas[t[1]] | pizzas[t[2]] | pizzas[t[3]]
    if t[0] == 4:
        uniqueValues = pizzas[t[1]] | pizzas[t[2]] | pizzas[t[3]] | pizzas[t[4]]
    
    score = len(uniqueValues) ** 2
    return score

def findBetterSolution(outputList, pizzas):
    for i in range(7000):
        # Get random team value
        x1 = r.randint(1, len(outputList) - 1)
        x2 = r.randint(1, len(outputList) - 1)

        # Get random pizza in of the team
        y1 = r.randint(1, len(outputList[x1]) - 1)
        y2 = r.randint(1, len(outputList[x2]) - 1)

        # Find old score of both teams
        scoreBefore = score(outputList[x1], pizzas) + score(outputList[x2], pizzas)

        outputList[x1][y1], outputList[x2][y2] = outputList[x2][y2], outputList[x1][y1]
        scoreAfter = score(outputList[x1], pizzas) + score(outputList[x2], pizzas)

        if scoreAfter < scoreBefore:
            outputList[x1][y1], outputList[x2][y2] = outputList[x2][y2], outputList[x1][y1]
    
    return outputList

def output(outputList, pizzaCounter):
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

def initialSolutionOptimization():
    numOfPizzas, numOf2, numOf3, numOf4, pizzas = parser()
    outputList, pizzaCounter = simpleApproach(pizzas, numOf2, numOf3, numOf4)
    outputList = findBetterSolution(outputList, pizzas)
    output(outputList, pizzaCounter)

# Execution
start = time.time()

initialSolutionOptimization()

end = time.time()
print("Execution time: {}".format(end - start))
print(end - start)