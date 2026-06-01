from construcao import alocar_demandas
from rotas import construir_rotas
import random

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

def selecao_torneio(populacao, k=3):
    torneio = random.sample(populacao, k)

    vencedor = min(torneio, key=lambda ind: ind["fitness"])

    return vencedor

import copy

# Adicionei o parametro dist, para recalcular o fitness depois da mutação
def mutacao(individuo, dist):
    rotas_validas = [r for r in individuo["rotas"] if len(r) > 3]

    if not rotas_validas:
        return individuo 

    rota = random.choice(rotas_validas)

    idx1, idx2 = random.sample(range(1, len(rota) - 1), 2)

    rota[idx1], rota[idx2] = rota[idx2], rota[idx1]
    
    # Adicionei recalculo do fitness, pq ele tava ficando desatualizado
    calcular_fitness(individuo, dist)

    return individuo

def crossover(pai1, pai2, demandas, capacidade, dist):
    seq1 = [c for rota in pai1["rotas"] for c in rota if c !=0]
    seq2 = [c for rota in pai2["rotas"] for c in rota if c!= 0]

    if tam < 2:
        return copy.deepcopy(pai1)
    
    tam = len(seq1)
    corte1, corte2 = sorted(random.sample(range(tam), 2))
    filho_seq = [None] * tam
    
    for i in range(corte1, corte2 + 1):
        filho_seq[i] = seq1[i]

    pos = 0

    for cliente in seq2:
        if cliente not in filho_seq:
            while filho_seq[pos] is not None:
                pos += 1
            filho_seq[pos] = cliente
    
    rotas = []
    rota_atual = [0]
    carga_atual = 0

    for cliente in filho_seq:
        demanda_cliente = demandas[cliente]
        if carga_atual + demanda_cliente <= capacidade:
            rota_atual.append(cliente)
            carga_atual += demanda_cliente
        
        else:
            rota_atual.append(0)
            rotas.append(rota_atual)

            rota_atual = [0, cliente]
            carga_atual = demanda_cliente

    rota_atual.append(0)
    rotas.append(rota_atual)

    filho = {
        "S": None,
        "rotas": rotas,
        "fitness": None
    }

    calcular_fitness(filho, dist)

    return filho

