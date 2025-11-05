import networkx as nx
from collections import deque

def bfs_nx(grafo, inicio, objetivo):
    fila = deque([[inicio]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        no = caminho[-1]

        if no == objetivo:
            return caminho

        if no not in visitados:
            visitados.add(no)
            for vizinho in grafo.neighbors(no):
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
    return None

# Exemplo
env = nx.Graph()
env.add_edges_from([('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')])

print("Caminho BFS:", bfs_nx(env, 'A', 'E'))
