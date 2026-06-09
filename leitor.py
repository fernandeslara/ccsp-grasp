import math

def calcular_distancia(p1, p2):
    return round(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

def carregar_instancia(caminho_completo, k_vizinhos):
    demandas = {}
    coordenadas = {}
    capacidade = 0
    
    with open(caminho_completo, 'r') as f:
        linhas = f.readlines()
        
    lendo_coordenadas = False
    lendo_demandas = False
    
    for linha in linhas:
        linha = linha.strip()
        # Pula linhas vazias
        if not linha:
            continue
            
        if ":" in linha:
            if linha.startswith("CAPACITY"):
                capacidade = int(linha.split(":")[1].strip())
            continue
            
        if not linha[0].isdigit() and not linha.startswith("-"):
            lendo_coordenadas = False
            lendo_demandas = False
            
            if "COORD" in linha:
                lendo_coordenadas = True
            elif "DEMAND" in linha:
                lendo_demandas = True
            continue
            
        if lendo_coordenadas:
            partes = linha.split()
            if len(partes) >= 3:
                idx = int(partes[0]) - 1 
                x = float(partes[1])
                y = float(partes[2])
                coordenadas[idx] = (x, y)
                demandas[idx] = 0 
                
        if lendo_demandas:
            partes = linha.split()
            if len(partes) >= 2:
                idx = int(partes[0]) - 1
                demandas[idx] = int(partes[1])

    n_vertices = len(coordenadas)
    
    dist = [[0.0 for _ in range(n_vertices)] for _ in range(n_vertices)]
    for i in range(n_vertices):
        for j in range(n_vertices):
            if i != j:
                dist[i][j] = calcular_distancia(coordenadas[i], coordenadas[j])
                
    U = [v for v in demandas if demandas[v] > 0 and v != 0]

    C = {u: [] for u in U}
    for v in range(n_vertices):
        vizinhos = sorted(range(n_vertices), key=lambda x: dist[v][x])
        k_mais_proximos = vizinhos[:k_vizinhos]
        
        for u in k_mais_proximos:
            if u in U:
                if v not in C[u]:
                    C[u].append(v)

    return U, demandas, capacidade, dist, C