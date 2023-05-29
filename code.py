import matplotlib.pyplot as plt
import numpy as np
import random
import time

INF = 999
s, e = 0, 0

# Algorithm 
def floyd(G):
    global s; s = time.time()
    
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    print_solution(distance)

    global e; e = time.time()
    
def print_solution(G):
    for i in range(len(G)):
        for j in range(len(G)):
            if(G[i][j] == INF):
                print("INF", end=" ")
            else:
                print(G[i][j], end="  ")
        print(" ")
        
def printGraph(G):
    for i in range(len(G)):
        v = i+1
        for j in range(len(G[i])):
            if G[i][j] != 0 and G[i][j] != 999: 
                print("V%d ---%d---> V%d" % (v, G[i][j], j+1))
            else: continue
        print()

def createGraph(size, case):
    G = [[random.randint(1, 20) for i in range(size)] for j in range(size)]
    
    for i in range(size):
        for j in range(size): 
            if i == j: G[i][j] = 0
            
    if case == "Best" or case == "Avg":
        if case == "Best":
            for i in range(size):
                for j in range(size):
                    if i != j: G[i][j] = random.randint(1, 20)
        elif case == "Avg":
            ran = [random.randint(0, size) for i in range(size)]
            for i in range(size):
                for j in range(size): 
                    if i != j and j == ran[i]: G[i][j] = 999
    elif case == "Worst":
        for i in range(size):
                for j in range(size): 
                    if j == i+1: G[i][j] = random.randint(1, 20)
                    elif i == j: G[i][j] = 0
                    elif i == size-1 and j == 0: G[i][j] = random.randint(1, 20)
                    else: G[i][j] = 999
    return np.array(G)

vertexNum = [5, 50, 100]
tBest, tAvg, tWorst = [], [], []

def drawCurve():
    plt.rcParams["figure.figsize"] = [12, 6]
    plt.xlabel("Number of Vertix")
    plt.ylabel("Running Time (microSec)")
   
    plt.grid(True)
    plt.plot(vertexNum, tBest, color='g', label="Best Case")
    plt.plot(vertexNum, tAvg,  color='y', label="Average Case")
    plt.plot(vertexNum, tWorst, color='r', label="Worst Case")
    
    plt.legend(loc="upper left")
    plt.show()
    


def testWorst():
    j = 1
    print(" \n \nWorst Case \n")
    for i in vertexNum:
        G = createGraph(i, "Worst")
        print("Senario %d: \n\tNumber of Vertex is %d" % (j, len(G))); floyd(G)
        print("\tRunning Time: %.5f microSec \n" % (1000000 * (e - s)))
        tWorst.append(1000000 * (e - s))
        j += 1 
    
def testBest():
    j = 1
    print(" \n \nBest Case \n")
    for i in vertexNum:
        G = createGraph(i, "Best")
        print("Senario %d: \n\tNumber of Vertex is %d" % (j, len(G))); floyd(G)
        print("\tRunning Time: %.5f microSec \n" % (1000000 * (e - s)))
        tBest.append(1000000 * (e - s))
        j += 1

def testAvg():
    j = 1
    print(" \n \nAverage Case \n")
    for i in vertexNum:
        G = createGraph(i, "Avg")
        if i == 5: print(G)
        print("Senario %d: \n\tNumber of Vertex is %d" % (j, len(G))); floyd(G)
        print("\tRunning Time: %.5f microSec \n" % (1000000 * (e - s)))
        tAvg.append(1000000 * (e - s))
        j += 1

testAvg(); testBest(); testWorst()
drawCurve()
