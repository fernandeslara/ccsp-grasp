from construcao import alocar_demandas
from rotas import construir_rotas

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