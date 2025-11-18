"""
graph_model.py
------------------------------------
Responsável por modelar o grafo utilizado no projeto.
Contém:
- Classe Graph (genérica)
- Funções utilitárias: adicionar nós, conexões, pesos
- Função de heurística (distância euclidiana)
- Função opcional de carregamento via JSON
------------------------------------
"""

import json
import math


class Graph:
    def __init__(self):
        # Estrutura:
        # { 'A': {'B': custo, 'C': custo}, ... }
        self.adjacency = {}

        # Para visualização com posições dos nós (opcional)
        # { 'A': (x, y), 'B': (x, y), ... }
        self.positions = {}

    # -------------------------------
    # Adicionar elementos ao grafo
    # -------------------------------

    def add_node(self, node, position=None):
        """Adiciona um nó ao grafo."""
        if node not in self.adjacency:
            self.adjacency[node] = {}

        if position:
            self.positions[node] = position

    def add_edge(self, node1, node2, cost, bidirectional=True):
        """Cria uma aresta com peso entre dois nós."""
        if node1 not in self.adjacency:
            self.add_node(node1)

        if node2 not in self.adjacency:
            self.add_node(node2)

        self.adjacency[node1][node2] = cost

        if bidirectional:
            self.adjacency[node2][node1] = cost

    # -------------------------------
    # Utilidades
    # -------------------------------

    def neighbors(self, node):
        """Retorna os vizinhos e seus custos."""
        return self.adjacency.get(node, {})

    def cost(self, node1, node2):
        """Retorna o custo (peso) entre dois nós."""
        return self.adjacency[node1][node2]

    # -------------------------------
    # Heurística
    # -------------------------------

    @staticmethod
    def heuristic(pos1, pos2):
        """
        Heurística padrão: distância euclidiana entre dois pontos.
        Usada pelo algoritmo A*.
        """
        (x1, y1) = pos1
        (x2, y2) = pos2
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # -------------------------------
    # Carregar grafo de arquivo JSON
    
    # -------------------------------

    @classmethod
    def from_json(cls, filepath):
        """
        Carrega o grafo de um arquivo JSON com a seguinte estrutura:
        {
            "nodes": {
                "A": [0, 0],
                "B": [1, 2]
            },
            "edges": [
                ["A", "B", 4],
                ["B", "C", 6]
            ]
        }
        """
        g = cls()

        with open(filepath, "r") as f:
            data = json.load(f)

        # Adiciona nós com posições
        for node, pos in data["nodes"].items():
            g.add_node(node, tuple(pos))

        # Adiciona arestas
        for n1, n2, cost in data["edges"]:
            g.add_edge(n1, n2, cost)

        return g


# ---------------------------------------
# Exemplo de uso simples (para testes)
# ---------------------------------------
if __name__ == "__main__":
    graph = Graph()

    # Criando um mini mapa manualmente
    graph.add_node("A", (0, 0))
    graph.add_node("B", (2, 1))
    graph.add_node("C", (4, 0))

    graph.add_edge("A", "B", 2)
    graph.add_edge("B", "C", 2)
    graph.add_edge("A", "C", 4)

    print("Nós:", graph.adjacency)
    print("Posições:", graph.positions)
