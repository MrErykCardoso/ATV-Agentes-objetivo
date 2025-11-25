import networkx as nx
from algorithms_search import aStar
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
            #função A* usando networkx
            self.path = aStar(self.graph, self.actual, self.goal); 
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