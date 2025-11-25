import networkx as nx;
import math;

# -------------------------------
# Heurística
# -------------------------------
def heuristic(pos1, pos2):
    """
    Heurística padrão: distância euclidiana entre dois pontos.
    Usada pelo algoritmo A*.
    """
    (x1, y1) = pos1
    (x2, y2) = pos2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def aStar(graph, actual, goal):
    # 1. Converter para networkx
    G = graph.to_networkx()

    # 2. Criar heurística adaptada para usar no networkx
    def heuristic_nx(u, v):
        return heuristic(graph.positions[u], graph.positions[v]);

    # 3. Executar A*
    path = nx.astar_path(G, actual, goal, heuristic=heuristic_nx, weight='weight');
    
    return path;