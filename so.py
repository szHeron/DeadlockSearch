from ReadFileEntry import ReadFileEntry

existingResources, disponibleResources, matrixAllocations, matrixResources, numberOfProcess = ReadFileEntry()
Deadlock = False

#Deadlocks por processos que requisitam mais que o total disponivel
def InsufficientResources():
    for processIndex,process in enumerate(matrixResources):
        for i, p in enumerate(process):
            if p > existingResources[i]:
                print(f"O processo P{processIndex+1} está em espera e aguardando {int(p-existingResources[i])} instancias de R{int(existingResources[i])}")
                return True
    return False

#Verificar se os recursos disponiveis suprem a requisição do processo
def EnoughtResources(process, temp):
    instances = []
    for i, p in enumerate(process):
        if p > temp[i]:
            instances.append(f'R{i+1} necessita de {int(p)} instancias, {temp[i]} disponiveis')
    return instances

#Função principal para fazer varredura em busca de deadlocks
def SearchDeadLocks():
    tempDisponibleResources = disponibleResources
    deadLockCounts = 0
    steps = 0
    for line in range(numberOfProcess):
        steps = 0
        for processIndex, process in enumerate(matrixResources):
            steps += 1
            instances = EnoughtResources(process, tempDisponibleResources)
            if len(instances) < 1:
                for i, x in enumerate(matrixAllocations[processIndex]):
                    tempDisponibleResources[i] += x
                    matrixAllocations[processIndex][i] = 0
            elif len(instances) > 0 and line+1 == numberOfProcess:
                deadLockCounts+=1
                print(f'Processo P{processIndex+1} em Deadlock ->')
                for j in instances:
                    print('\t',j)
    if deadLockCounts > 0:
        return True
    else:
        return False

Deadlock = InsufficientResources()
if not Deadlock:
    Deadlock = SearchDeadLocks()
    if not Deadlock:
        print("Todos os processos estão finalizados!")