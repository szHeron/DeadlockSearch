from ReadFileEntry import ReadFileEntry

existingResources, disponibleResources, matrixAllocations, matrixRequistions, numberOfProcess = ReadFileEntry()

#Verificar se os recursos disponiveis suprem a requisição do processo
def EnoughtResources(process, temp):
    instances = []
    for i, p in enumerate(process):
        #Verifico se a requisição do processo é maior que a quantidade de recursos disponiveis, se sim insiro no array de instancias
        if p > temp[i]:
            instances.append(f'R{i+1} necessita de {int(p) - temp[i]} instancias')
    return instances

#Função principal para fazer varredura em busca de deadlocks
def SearchDeadLocks():
    #Contador de deadlocks
    deadLockCounts = 0

    #Instancia de recursos em espera
    globalInstances = []

    #For é executado pela quantidade de processos existentes, ou seja, 
    #toda vez que um processo é ou não executado, chega mais proximo de se encerrar
    for line in range(numberOfProcess):
        #Passar em todos os processos da matriz de requisições, analisando qual processo deve ser executado
        for processIndex, process in enumerate(matrixRequistions):
            #Retorna as instancias de requisição caso o processo esteja em espera ou em deadlock
            instances = EnoughtResources(process, disponibleResources)

            if len(instances) < 1:  
                #Se não houver instancias de requisições pendentes, será descontado da matriz de alocações e incrementado nos recursos disponiveis
                for i, x in enumerate(matrixAllocations[processIndex]):
                    disponibleResources[i] += x
                    matrixAllocations[processIndex][i] = 0
            elif len(instances) > 0 and line + 1 == numberOfProcess:
                #Se houver instancias de requisições pendentes, será guardado para mostrar nos resultados
                instances.insert(0,processIndex+1)
                globalInstances.append(instances)
                #Incrementado o contador de deadlock
                deadLockCounts+=1

    #Exibir resultados
    if deadLockCounts > 0:
        for x in globalInstances:
            for index, y in enumerate(x):
                if index == 0:
                    if deadLockCounts == 1:
                        print(f'Processo P{y} em ESPERA ->')
                    else:
                        print(f'Processo P{y} em DEADLOCK ->')
                else:
                    print('\t', y)
        return True
    else:
        print("Todos os processos estão finalizados!")
        return False

SearchDeadLocks()
