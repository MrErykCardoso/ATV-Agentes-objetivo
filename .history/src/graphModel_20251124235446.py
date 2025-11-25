import json
import math
import networkx as nx


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
    # Carregar grafo de arquivo JSON
    # Esse trecho é opcional, será utilizado apenas se usarmos arquivos json
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
    
    def to_networkx(self):
         G = nx.Graph()

    # adicionar nós
        for node, pos in self.positions.items():
            G.add_node(node, pos=pos)

    # adicionar arestas sem duplicar
    for n1, vizinhos in self.adjacency.items():
        for n2, cost in vizinhos.items():
            if not G.has_edge(n1, n2):
                G.add_edge(n1, n2, weight=cost)

        return G
            
        