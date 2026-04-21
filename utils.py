import random

def construir_LRC(candidatos, custos, alpha):
    c_min = min(custos)
    c_max = max(custos)

    l = c_min + alpha * (c_max - c_min)

    LRC = []

    for i in range(len(candidatos)):
        if custos[i] <= l:
            LRC.append(candidatos[i])

    return LRC


def selecionar_aleatorio(LRC):
    return random.choice(LRC)