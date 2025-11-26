import networkx as nx
from algorithms_search import aStar
from graphModel import Graph
from decorations import *


class Agent:
    def __init__(self, graph, start, goal):
        self.graph = graph; # grafo do ambiante
        self.start = start;  # posição atual
        self.goal = goal; # objetivo
        self.path = []; # caminho planejado
        
    def selfPerception(self):
        """Função para perceber os arredores (Posição atual, visinho, etc)"""
        return list(self.graph.neighbors(self.start));
    
    def plan(self):
        """Função para o planejamento de tragetória para ação"""
        try:
            #função A* usando networkx
            loading("Planejando rota")
            self.path = aStar(self.graph, self.start, self.goal); 
            listar_opcoes("Trajetória criada!\nSequência de nós: ", self.path);
        except Exception as e:
            erroPrint(f"\nNenhum caminho encontrado.\nErro: {e}");
            
    def act(self):
        """Execução do plano"""
        doPath = list(self.path)
        actual = self.start
        
        if not doPath:
            erroPrint("\nImpossível prosseguir:\nNenhum plano foi traçado ainda!");
            return;
        
        while(actual != self.goal):
            if doPath and actual != self.goal:
                doPath.pop(0); 
                if doPath:
                    actual = doPath[0];
                    print(f"\nPosição atualizada para: {actual};");

        okPrint(f"Objetivo atingido!\nPosição atual: {actual};\nPosição pretendida: {self.goal};");
        return;