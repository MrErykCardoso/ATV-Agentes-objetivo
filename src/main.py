import os
import matplotlib.pyplot as plt
import networkx as nx
from agent import Agent
from graphModel import Graph
from decorations import *

"""Sequência para armazenar o caminho da pasta data a partir da localização do main."""
CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CURRENT_DIR)
DATA_PATH = os.path.join(ROOT_DIR, 'data')

def jsonList():
    
    """Usa o caminho da pasta data para verificar e armazenar uma lista de arquivos contidos dentro dela com a terminação .json."""
    
    #Faz uma varredura com o for e retorna uma lista de arquivos com terminação .json
    return [f for f in os.listdir(DATA_PATH) if f.endswith(".json")]

def graphChoice():
    
    """Usa a lista gerada na função do jsonList para imprimir a sequência de arquivos .json e permitir ao usuário escolher qual 'mapa' deseja explorar."""
    jsons = jsonList()
    titulo("Escolha um grafo")
    listar_opcoes("Grafos disponíveis:", jsons)
    idx = int(prompt("Digite o índice do grafo"))
    
    #Retorna o caminho do grafo escolhido
    return os.path.join(DATA_PATH, jsons[idx])

def nodeChoice(grafo):
    
    """Com base no grafo.json escolhido na função graphChoice, recebe uma lista de nós do grafo e permite ao usuário escolher o início e o objetivo da tragetória."""
    nodes = list(grafo.adjacency.keys())
    titulo("Selecione os nós")
    listar_opcoes("Nós disponíveis:", nodes)
    actual = nodes[int(prompt("Escolha o nó de início"))]
    goal = nodes[int(prompt("Escolha o nó objetivo"))]
    
    #Retorna as posições selecionadas pelo usuário
    return actual, goal

def plotGraph(graph, path):
    """Recebe o grafo escolhido e o caminho gerado pelo algorítmo de busca para construir um grafo networkx com características de cor dos nós e arestas para imprimir com o matplotlib."""
    #Gera uma instância vasia de grafo networx
    G = nx.Graph()
    
    #Faz uma varredura na lista de pisições contidas no objeto gerado pela classe Graph e adiciona os nós e suas posições no grafo networkx
    for node, pos in graph.positions.items():
        G.add_node(node, pos=pos)
    
    #Faz uma verredura das arestas e seus pesos e adiciona no networkx
    for node, neighbors in graph.adjacency.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)
    
    #Coleta as posições dos nós do grafo networkx
    pos = nx.get_node_attributes(G, "pos")
    
    #Se não ouver posições, gera um modelo padrão do networkx
    if not pos:
        pos = nx.spring_layout(G)

    #Desenha o grafo e suas posições
    nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=12)
    
    #Desenha as arestas entre os nós e destaca o caminho percorrido pelo agente
    if path and len(path) > 1:
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=3, edge_color="red")

    #Matplotlib desenha os grafo e mostra em janela paralela.
    loading()
    okPrint("Dados carregados para o MATPLOTLIB;\nFeche a janela paralela para continuar")
    plt.show()

def main():
    """Função de chamada de todas as outras funções em sequência de apresentação para o usuário."""
    opt = 1
    while(opt == 1):
        try:
            #1) Apresenta o programa e pede pela seleção do grafo
            clear()
            loading()
            titulo("Sistema de Navegação com A*")
            graphJson = graphChoice()
            loading("Carregando grafo")
            graph = Graph.from_json(graphJson)
            
            #2) Pede pela seleção dos nós de início e fim
            clear()
            actual, goal = nodeChoice(graph)
            loading("Configurando agente")

            #3) Criação do agente e chamada de funções de planejamento e execução de rota
            clear()
            agent = Agent(graph, actual, goal)
            titulo("Planejamento da Rota")
            agent.plan()
            titulo("Execução da Rota")
            agent.act()
            
            #3.5) Verifica o destino e dá um status de sucesso ou fracasso
            perigos = ["PenhascoDoGavioes", "BosqueDoGuapardo"]
            riscos = ["CampoDoBode", "PlanicieH",]
            montanha = "MontanhaAlta"
            if graphJson.endswith("patinhos.json") and agent.goal in perigos:
                erroPrint("\n\nOs patinhos viraram almoço de uma fera selvagem")
            elif graphJson.endswith("patinhos.json") and agent.goal in riscos:
                erroPrint("\n\nUm animal herbivoro acidentalmente pisoteou os patinhos.\nFoi o fim deles")
            elif graphJson.endswith("patinhos.json") and agent.goal in montanha:
                erroPrint("\n\nOs patinhos acidentalmente cairam de uma altura enorme.\nInfelizmente eles ainda não sabiam voar")
            else: 
                okPrint("\n\nOs patinhos foram passear e voltaram com sucesso apra casa.\nA mamãe está contente")
            
            #4) Caso seja possível gerar uma rota, plota o gráfico e a trajetória para visualisação em janela paralela.
            if agent.path:
                titulo("Visualização do Caminho")
                plotGraph(graph, agent.path)

        except Exception as e:
            loading()
            clear()
            erroPrint(f"Inserção inválida!\nErro: {e}\n\nA inserção de um dado incorreto compromete a funcionalidade do agente.\nPor favor tente novamente e siga as instruções corretamente")

        #5) Pergunta se o usuário deseja continuar e prende no laço para tratamento de exceções.S
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
