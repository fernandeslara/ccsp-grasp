from construcao import *
from rotas import *
from dados import *
from utils import *
from genetico import *
import random

ind = criar_individuo(
    U,
    demandas,
    capacidade,
    alpha,
    beta,
    C,
    dist
)

print("INDIVÍDUO GERADO:\n")

print("Alocação (S):")
print(ind["S"])

print("\nRotas:")
print(ind["rotas"])

print("\nFitness:")
print(ind["fitness"])