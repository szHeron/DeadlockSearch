import numpy as np

def ReadFileEntry():
    file = open('entrada.txt', 'r')
    numberOfProcess = int(file.readline(1))
    resources = int(file.readline(3))
    matrixAllocations = np.zeros((numberOfProcess, resources))
    matrixResources = np.zeros((numberOfProcess, resources))
    existingResources = []
    disponibleResources = []
    espaces = 0
    steps = 0

    for line in file:
        if len(line) == 1:
            espaces += 1
            steps = 0
        else:
            line = line.split()
            if espaces == 1:
                existingResources = list(map(int, line))
            elif espaces == 2:
                disponibleResources = list(map(int, line))
            elif espaces == 3:
                matrixAllocations[steps] = [int(numeric_string) for numeric_string in line]
                steps += 1
            elif espaces == 4:
                matrixResources[steps] = [int(numeric_string) for numeric_string in line]
                steps += 1
                
    file.close()
    return existingResources, disponibleResources, matrixAllocations, matrixResources, numberOfProcess