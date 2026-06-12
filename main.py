from construcao import *
from rotas import *
from leitor import carregar_instancia
from utils import *
from genetico import *
import random
import copy

TAMANHO_POP = 100 
NUM_GERACOES = 200 
TAXA_MUTACAO = 0.6

caminho_arquivo = "./Instances_Uchoa_et_al/X-n298-kX-w118-c7.cctp"

print("Carregando instância...")

U, demandas, capacidade, dist, C = carregar_instancia(caminho_arquivo, k_vizinhos=7)

alpha = 0.5
beta = 0.5

print("Gerando população inicial...")
populacao = gerar_populacao(TAMANHO_POP, U, demandas, capacidade, alpha, beta, C, dist)
print("Iniciando evolução...\n")

for geracao in range(NUM_GERACOES):
    nova_populacao = []
    
    melhor_atual = min(populacao, key=lambda ind: ind["fitness"])
    nova_populacao.append(copy.deepcopy(melhor_atual))
    
    while len(nova_populacao) < TAMANHO_POP:
        pai1 = selecao_torneio(populacao)
        pai2 = selecao_torneio(populacao)
        
        filho = crossover(pai1, pai2, demandas, capacidade, dist, C)
        
        if random.random() < TAXA_MUTACAO:
            mutacao(filho, dist, demandas, capacidade, C) 
            
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