import networkx as nx
import algorithms_search as a
from graphModel import Graph


class Agent:
    def __init__(self, graph, actual, goal):
        self.graph = graph; # grafo do ambiante
        self.actual = actual;  # posição atual
        self.goal = goal; # objetivo
        self.path = []; # caminho planejado
        
    def selfPerception(self):
        """Função para perceber os arredores (Posição atual, visinho, etc)"""
        return list(self.graph.neighbors(self.actual));
    
    def plan(self):
        """Função para o planejamento de tragetória para ação"""
        try:
            #self.path = a.aStar(self.graph, self.actual, self.goal); #função separada de A* usando networkx
            # 1. Converter para networkx
            G = self.graph.to_networkx()

            # 2. Criar heurística adaptada
            heuristic = lambda u, v: Graph.heuristic(
                self.graph.positions[u], 
                self.graph.positions[v]
            )

            # 3. Executar A*
            self.path = nx.astar_path(G, self.actual, self.goal, heuristic=heuristic, weight='weight')
            print(f"Plano traçado: {self.path}");
        except Exception as e:
            print(f"Nenhum caminho encontrado. Erro: {e}");
            
    def act(self):
        """Execução do plano"""
        if not self.path:
            print("\n\nImpossível prosseguir: Nenhum plano foi traçado ainda!");
            return;
        
        print(f"\n\nCaminho planejado: {self.path};");        
        while(self.actual != self.goal):
            
            if self.path and self.actual != self.goal:
                self.path.pop(0); 
                if self.path:
                    self.actual = self.path[0];
                    print(f"Posição atualizada para: {self.actual};");

        print(f"Objetivo atingido!\nPosição atual: {self.actual};\nPosição pretendida: {self.goal};");
        return;