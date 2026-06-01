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

def mutacao(individuo):
    rotas_validas = [r for r in individuo["rotas"] if len(r) > 3]

    if not rotas_validas:
        return individuo 

    rota = random.choice(rotas_validas)

    idx1, idx2 = random.sample(range(1, len(rota) - 1), 2)

    rota[idx1], rota[idx2] = rota[idx2], rota[idx1]

    return individuo
