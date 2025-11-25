import os
import matplotlib.pyplot as plt
import networkx as nx
from agent import Agent
from graphModel import Graph

CURRENT_DIR = os.path.dirname(__file__);
ROOT_DIR = os.path.dirname(CURRENT_DIR);
DATA_PATH = os.path.join(ROOT_DIR, 'data');

def jsonList():
    """Cria lista de grafos contidos na pasta data na raiz do projeto."""
    arquives = os.listdir(DATA_PATH);
    jsons = [file for file in arquives if file.endswith(".json")];
    return jsons;
    
def graphChoice():
    """Auxilia na seleção do grafo pelo usuário."""
    jsons = jsonList();
    
    print("\n\n----- Escolha qual grafo deseja esplorar: ----- ");
    for i, nome in enumerate(jsons):
        print(f"({i}): {nome};");
    choice = int(input("\nDigite o índice do grafo (0, 1, 2, ...): "));
    
    return os.path.join(DATA_PATH, jsons[choice]);
    
def nodeChoice(grafo):
    """Auxilia na seleção dos nós ded início e objetivo pelo usuário."""
    nodes = list(grafo.adjacency.keys());
    
    print("\n\n----- Escolha dentre os nós abaixo: -----");
    i = 0;
    for node in nodes:
        print(f"({i}): {node}");0
        i = i + 1;
    actual = nodes[int(input("\nEscolha o índice do nó de início (0, 1, 2, ...): "))];
    goal = nodes[int(input("\nEscolha o índice do nó de objetivo(0, 1, 2, ...): "))];
    
    return actual, goal;
    
def plotGraph(graph, path):
    """Usa o nx.Graph() e o matplotlib para criar a plotagem do grafo selecionado."""
    G = nx.Graph()
    
    # 1. Adicionar nós com posição correta
    for node, pos in graph.positions.items():
        G.add_node(node, pos=pos)
    
    # 2. Adicionar arestas
    for node, neighbors in graph.adjacency.items():
        for neighbor, cost in neighbors.items():
            if (neighbor, node) not in G.edges():
                G.add_edge(node, neighbor, weight=cost)

    
    # 3. Pegar as posições
    pos = nx.get_node_attributes(G, "pos")

    # 4. Se não houver posições, usar spring_layout
    if not pos:
        pos = nx.spring_layout(G)

    # 5. Desenhar grafo
    nx.draw(
        G, pos, with_labels=True,
        node_size=800, node_color="lightblue",
        font_size=12
    )

    # 6. Desenhar caminho em vermelho
    if path and len(path) > 1:
        caminho_arestas = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            G, pos,
            edgelist=caminho_arestas,
            width=3,
            edge_color="red"
        )

    plt.show()
    
def main():
    """Esecuta as funções do menu de intereação com o usuário."""
    #1) Escolher grafo:
    graphJson = graphChoice();
    0
    #2) Criar o grafo:
    graph = Graph.from_json(graphJson);
    
    #3) Escolher nós de início e objetivo:
    actual, goal = nodeChoice(graph);
    
    #4) Criar agente:
    agent = Agent(graph, actual, goal);
    
    #5) Planejar caminho:
    agent.plan();
    
    #6) Executar plano:
    agent.act();
    
    #7) Plotar grafo e execução:
    if agent.path:
        plotGraph(graph, agent.path);

if __name__ == "__main__":
    main();
        