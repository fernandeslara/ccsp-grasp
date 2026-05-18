from construcao import *
from rotas import *
from dados import *
from utils import *
from genetico import *
import random
import copy

TAMANHO_POP = 20
NUM_GERACOES = 50
TAXA_MUTACAO = 0.4 

print("Gerando população inicial...")
populacao = gerar_populacao(TAMANHO_POP, U, demandas, capacidade, alpha, beta, C, dist)

print("Iniciando evolução...\n")

for geracao in range(NUM_GERACOES):
    nova_populacao = []
    
    melhor_atual = min(populacao, key=lambda ind: ind["fitness"])
    nova_populacao.append(copy.deepcopy(melhor_atual))
    
    while len(nova_populacao) < TAMANHO_POP:
        pai = selecao_torneio(populacao)
        
        filho = copy.deepcopy(pai)
        
        if random.random() < TAXA_MUTACAO:
            mutacao(filho)
            calcular_fitness(filho, dist)
            
        nova_populacao.append(filho)
        
    populacao = nova_populacao

    if (geracao + 1) % 10 == 0:
        melhor_da_geracao = min(populacao, key=lambda ind: ind["fitness"])
        print(f"Geração {geracao + 1} | Melhor Fitness: {melhor_da_geracao['fitness']}")

melhor_solucao_global = min(populacao, key=lambda ind: ind["fitness"])

print("\n=== MELHOR SOLUÇÃO ENCONTRADA ===")
print("Alocação (S):", melhor_solucao_global["S"])
print("Rotas:", melhor_solucao_global["rotas"])
print("Fitness:", melhor_solucao_global["fitness"])
print("INDIVÍDUO GERADO:\n")