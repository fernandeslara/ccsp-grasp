from construcao import *
from rotas import *
from dados import *
from utils import *
import random

def teste_alocacao_debug():
    random.seed(0)

    S = []
    U_local = U.copy()
    cargas_local = []

    passo = 1

    while len(U_local) > 0:
        print(f"\n====== PASSO {passo} ======")
        print("U:", U_local)
        print("S:", S)
        print("cargas:", cargas_local)

        candidatos = gerar_candidatos_alocacao(U_local, S, demandas, capacidade, cargas_local)
        print("\nCandidatos:", candidatos)

        custos = calcular_custos_alocacao(candidatos, demandas, capacidade, cargas_local)
        print("Custos:", custos)

        LRC = construir_LRC(candidatos, custos, alpha)
        print("LRC:", LRC)

        e = selecionar_aleatorio(LRC)
        print("Escolhido (e):", e)

        aplicar_alocacao(e, S, cargas_local, demandas)
        print("Novo S:", S)

        remover_demanda(e, U_local)

        passo += 1

    print("\n=== RESULTADO FINAL ===")
    print("S final:", S)


def teste_rotas_debug():
    random.seed(0)

    S = [[0, 1], [2]]

    print("\n=== TESTE ROTAS ===")

    for m in S:
        print("\n--- Veículo ---", m)

        rm = [0, 0]
        print("Rota inicial:", rm)

        for u in m:
            print("\nDemanda:", u)

            candidatos = gerar_candidatos_insercao(u, rm, C)
            print("Candidatos:", candidatos)

            if not candidatos:
                continue

            custos = calcular_custos_insercao(candidatos, rm, dist)
            print("Custos:", custos)

            LRC = construir_LRC(candidatos, custos, beta)
            print("LRC:", LRC)

            v = selecionar_aleatorio(LRC)
            print("Escolhido:", v)

            inserir_na_rota(v, rm, dist)
            print("Rota atual:", rm)

        print("\nRota final:", rm)


if __name__ == "__main__":
    teste_alocacao_debug()
    teste_rotas_debug()