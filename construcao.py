from utils import construir_LRC, selecionar_aleatorio

def alocar_demandas(alpha, U, demandas, capacidade, cargas):

    S = []

    while len(U) > 0:
        candidatos = gerar_candidatos_alocacao(U, S, demandas, capacidade, cargas)

        custos = calcular_custos_alocacao(candidatos, demandas, capacidade, cargas)

        LRC = construir_LRC(candidatos, custos, alpha)

        e = selecionar_aleatorio(LRC)

        aplicar_alocacao(e, S, cargas, demandas)

        remover_demanda(e, U)

    return S


def gerar_candidatos_alocacao(U, S, demandas, capacidade, cargas):
    candidatos = []

    for u in U:
        for i in range(len(S)):
            if cargas[i] + demandas[u] <= capacidade:
                candidatos.append((u, i))

        candidatos.append((u, len(S)))

    return candidatos


def calcular_custos_alocacao(candidatos, demandas, capacidade, cargas):
    custos = []

    for (u, m) in candidatos:
        if m < len(cargas):
            carga_atual = cargas[m]
        else:
            carga_atual = 0

        capacidade_restante = capacidade - (carga_atual + demandas[u])
        custos.append(capacidade_restante)

    return custos


def aplicar_alocacao(e, S, cargas, demandas):
    u, m = e

    if m < len(S):
        S[m].append(u)
        cargas[m] += demandas[u]
    else:
        S.append([u])
        cargas.append(demandas[u])


def remover_demanda(e, U):
    u, _ = e
    if u in U:
        U.remove(u)