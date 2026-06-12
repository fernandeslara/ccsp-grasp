from construcao import alocar_demandas
from rotas import construir_rotas
import random
import copy

def criar_individuo(U, demandas, capacidade, alpha, beta, C, dist):
    U_local = U.copy()
    cargas = []

    S = alocar_demandas(alpha, U_local, demandas, capacidade,cargas)
    rotas = construir_rotas(S, beta, C, dist)

    individuo = {
        "S": S, 
        "rotas": rotas,
        "fitness": None
    }
    
    calcular_fitness(individuo, dist)

    return individuo

def calcular_fitness(individuo, dist):
    custo_total = 0

    for rota in individuo["rotas"]:
        for i in range(len(rota) - 1):
            a = rota[i]
            b = rota[i + 1]

            custo_total += dist[a][b]
    
    individuo["fitness"] = custo_total

    return custo_total

def gerar_populacao(tamanho_populacao, U, demandas, capacidade, alpha, beta, C, dist):
    populacao = []

    for _ in range(tamanho_populacao):
        ind = criar_individuo(U, demandas, capacidade, alpha, beta, C, dist)
        populacao.append(ind)

    return populacao

def selecao_torneio(populacao, k=2):
    torneio = random.sample(populacao, k)

    vencedor = min(torneio, key=lambda ind: ind["fitness"])

    return vencedor

def mutacao(individuo, dist, demandas, capacidade, C):
    S = individuo["S"]
    if len(S) < 2:
        return individuo
        
    v1, v2 = random.sample(range(len(S)), 2)
    
    if not S[v1]: 
        return individuo
        
    u = random.choice(S[v1])
    
    carga2 = sum(demandas[cliente] for cliente in S[v2])
    if carga2 + demandas[u] <= capacidade:
        S[v1].remove(u)
        S[v2].append(u)
        
        individuo["S"] = [v for v in S if v]
        
        from rotas import construir_rotas
        individuo["rotas"] = construir_rotas(individuo["S"], 0.5, C, dist)
        calcular_fitness(individuo, dist)
        
    return individuo

def crossover(pai1, pai2, demandas, capacidade, dist, C):
    S1 = pai1["S"]
    S2 = pai2["S"]
    
    if not S1:
        return copy.deepcopy(pai1)
        
    veiculo_herdado = random.choice(S1)
    S_filho = [veiculo_herdado.copy()]
    clientes_alocados = set(veiculo_herdado)
    
    for veiculo_p2 in S2:
        novo_veiculo = []
        for u in veiculo_p2:
            if u not in clientes_alocados:
                novo_veiculo.append(u)
                clientes_alocados.add(u)
        
        if novo_veiculo:
            S_filho.append(novo_veiculo)
            
    rotas_filho = construir_rotas(S_filho, 0.5, C, dist)
    
    filho = {
        "S": S_filho,
        "rotas": rotas_filho,
        "fitness": None
    }
    
    calcular_fitness(filho, dist)
    return filho