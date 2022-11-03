import numpy as np

def ReadFileEntry():
    file = open('entrada.txt', 'r')
    arq = file.readline()
    numberOfProcess = int(arq.split()[0])
    resources = int(arq.split()[1])
    matrixAllocations = np.zeros((numberOfProcess, resources))
    matrixRequistions = np.zeros((numberOfProcess, resources))
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
                matrixRequistions[steps] = [int(numeric_string) for numeric_string in line]
                steps += 1
                
    file.close()
    return existingResources, disponibleResources, matrixAllocations, matrixRequistions, numberOfProcess