import os
import matplotlib.pyplot as plt
import networkx as nx
from agent import Agent
from graphModel import Graph
from decorations import *

CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CURRENT_DIR)
DATA_PATH = os.path.join(ROOT_DIR, 'data')

def jsonList():
    return [f for f in os.listdir(DATA_PATH) if f.endswith(".json")]

def graphChoice():
    jsons = jsonList()
    titulo("Escolha um grafo")
    listar_opcoes("Grafos disponíveis:", jsons)
    idx = int(prompt("Digite o índice do grafo"))
    return os.path.join(DATA_PATH, jsons[idx])

def nodeChoice(grafo):
    nodes = list(grafo.adjacency.keys())
    titulo("Selecione os nós")
    
    listar_opcoes("Nós disponíveis:", nodes)
    
    actual = nodes[int(prompt("Escolha o nó de início"))]
    goal = nodes[int(prompt("Escolha o nó objetivo"))]
    return actual, goal

def plotGraph(graph, path):
    G = nx.Graph()

    for node, pos in graph.positions.items():
        G.add_node(node, pos=pos)

    for node, neighbors in graph.adjacency.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.get_node_attributes(G, "pos")
    if not pos:
        pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=12)
    
    if path and len(path) > 1:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=3, edge_color="red")

    loading()
    okPrint("Dados carregados para o MATPLOTLIB;\nFeche a janela paralela para continuar")
    plt.show()

def main():
    opt = 1
    while(opt == 1):
        clear()
        loading()
        titulo("Sistema de Navegação com A*")
        graphJson = graphChoice()
        loading("Carregando grafo")
        graph = Graph.from_json(graphJson)
        
        clear()
        actual, goal = nodeChoice(graph)
        loading("Configurando agente")

        clear()
        agent = Agent(graph, actual, goal)
        titulo("Planejamento da Rota")
        agent.plan()
        titulo("Execução da Rota")
        agent.act()

        if agent.path:
            titulo("Visualização do Caminho")
            plotGraph(graph, agent.path)
        
        cho = 2
        while(cho != 0 or cho != 1):
            try:
                titulo("")
                cho = int(prompt("\n\nGostaria de tentar novamente (1 - sim; 0 - não) ? "))
                loading()
                
                clear()
                if(cho == 1):
                    opt = 1
                    break
                elif(cho == 0):
                    opt = 0
                    break
                else:
                    erroPrint("\n\nInserção inválida.\nPor favor insira uma das opções indicadas.")
            except Exception as e:
                clear()
                erroPrint(f"\n\nInserção inválida.\nErro: {e};\nPor favor insira uma das opções indicadas.")
                

if __name__ == "__main__":
    main()
