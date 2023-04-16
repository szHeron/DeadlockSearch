from ReadFileEntry import ReadFileEntry

existingResources, disponibleResources, matrixAllocations, matrixRequistions, numberOfProcess = ReadFileEntry()

def EnoughtResources(process, temp):
    instances = []
    for i, p in enumerate(process):
        if p > temp[i]:
            instances.append(f"R{i+1} necessita de {int(p) - temp[i]} instancias")
    return instances

def SearchDeadLocks():
    deadLockCounts = 0
    globalInstances = []

    for line in range(numberOfProcess):
        for processIndex, process in enumerate(matrixRequistions):
            instances = EnoughtResources(process, disponibleResources)
            if len(instances) < 1:  
                for i, x in enumerate(matrixAllocations[processIndex]):
                    disponibleResources[i] += x
                    matrixAllocations[processIndex][i] = 0
            elif len(instances) > 0 and line + 1 == numberOfProcess:
                instances.insert(0,processIndex+1)
                globalInstances.append(instances)
                deadLockCounts+=1

    if deadLockCounts > 0:
        for x in globalInstances:
            for index, y in enumerate(x):
                if index == 0:
                    if deadLockCounts == 1:
                        print(f"Processo P{y} em ESPERA ->")
                    else:
                        print(f"Processo P{y} em DEADLOCK ->")
                else:
                    print('\t', y)
        return True
    else:
        print("Todos os processos estão finalizados!")
        return False

SearchDeadLocks()
