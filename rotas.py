from utils import construir_LRC, selecionar_aleatorio

def construir_rotas(S, beta, C, dist):
    rotas = []
    for m in S:
        rm = [0, 0]  # depósito
        for u in m:
            candidatos = gerar_candidatos_insercao(u, rm, C)
            if not candidatos: 
                continue
            custos = calcular_custos_insercao(candidatos, rm, dist)
            LRC = construir_LRC(candidatos, custos, beta)
            v = selecionar_aleatorio(LRC)
            inserir_na_rota(v, rm, dist)
        rotas.append(rm)
    return rotas

def gerar_candidatos_insercao(u, rm, C):
    candidatos = []
    for v in C[u]:
        if v not in rm:
            candidatos.append(v)
    return candidatos

def calcular_custos_insercao(candidatos, rm, dist):
    custos = []
    for v in candidatos:
        melhor_custo = float('inf')
        for i in range(len(rm) - 1):
            custo = dist[rm[i]][v] + dist[v][rm[i+1]] - dist[rm[i]][rm[i+1]]
            if custo < melhor_custo:
                melhor_custo = custo
        custos.append(melhor_custo)
    return custos

def inserir_na_rota(v, rm, dist):
    melhor_pos = 0
    melhor_custo = float('inf')
    for i in range(len(rm) - 1):
        custo = dist[rm[i]][v] + dist[v][rm[i+1]] - dist[rm[i]][rm[i+1]]
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_pos = i + 1
    rm.insert(melhor_pos, v)