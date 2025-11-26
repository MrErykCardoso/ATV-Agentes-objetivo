
# **Agentes Baseados em Objetivo (A*)**

### *Sistema de Navegação Inteligente usando Grafos, JSON e A**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![IA](https://img.shields.io/badge/AI-Agent%20Based%20Modeling-orange.svg?style=for-the-badge)
![A*](https://img.shields.io/badge/Algorithm-A*%20Search-red.svg?style=for-the-badge)


### Fluxograma do Funcionamento
~~~
───────────────────────────────────────────────────────────────────────────────
                                ██╗ █████╗ 
                                ██║██╔══██╗
                                ██║███████║
                                ██║██╔══██║
                                ██║██║  ██║
                                ╚═╝╚═╝  ╚═╝
──────────────────────────  INÍCIO DO PROGRAMA  ───────────────────────────────

                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║                           EXIBIR MENU DE GRAFOS                            ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║                         USUÁRIO SELECIONA O JSON                           ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║       CARREGAR GRAFO → Graph.from_json(filepath)                           ║
║       • Carrega nós                                                        ║
║       • Carrega posições                                                   ║
║       • Carrega arestas                                                    ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║          LISTAR NÓS → Usuário escolhe início e objetivo                    ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║            CRIAR AGENTE → Agent(graph, actual, goal)                       ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║                       PLANEJAMENTO (A*) → plan()                            ║
║                  path = aStar(graph, actual, goal)                          ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║                   EXECUÇÃO DO PLANO → act()                                 ║
║             Caminho percorrido passo a passo pelo agente                    ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
╔═════════════════════════════════════════════════════════════════════════════╗
║   PLOTAGEM DO GRAFO → plotGraph()                                           ║
║   • Desenha nós                                                             ║
║   • Desenha arestas                                                         ║
║   • Destaca o caminho encontrado em vermelho                                ║
╚═════════════════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
───────────────────────────────  FIM DA EXECUÇÃO  ─────────────────────────────

~~~

## Vídeo da Apresentação

A apresentação completa do trabalho pode ser assistida no link abaixo:

👉 **YouTube:** https://www.youtube.com/watch?v=8bTg79S32u4


## **Descrição do Projeto**

Este projeto implementa um **agente baseado em objetivo** capaz de:

* carregar grafos a partir de arquivos JSON
* permitir ao usuário escolher o mapa
* selecionar o nó inicial e o objetivo
* planejar o caminho usando **A***
* executar o plano movendo-se passo a passo
* exibir graficamente o grafo 

Tudo isso utilizando:

* **Python 3**
* **NetworkX**
* **Matplotlib**

📂 **Estrutura do Projeto**
~~~
  ATV-Agentes-Objetivo/
  │
  ├── data/
  │   ├── mapaComplexo.json
  │   ├── mapaMedio.json
  │   └── patinhos.json
  │
  ├── docs/
  │   └── descrição-da-atv.txt
  │
  ├── src/
  │   ├── main.py
  │   ├── agent.py
  │   ├── algorithms_search.py
  │   └── graphModel.py
  │
  ├── README.md
  └── requirements.txt
~~~

## **Instalação**

### 1️⃣ Instalar dependências

No terminal:
~~~
pip install -r requirements.txt
~~~

## **Como Executar o Sistema**

### 1️⃣ Entre na pasta raiz do projeto:
~~~
cd ATV-Agentes-objetivo
~~~
Rode o arquivo principal:
~~~
python src/main.py
~~~

## **1. Escolha do Grafo**

O sistema lista automaticamente os grafos disponíveis dentro da pasta `/data`.

Exemplo:
~~~
----- Escolha qual grafo deseja explorar: -----
(0): patinhos.json
(1): mapaMedio.json
(2): mapaComplexo.json
~~~
Você escolhe pelo índice, como:
~~~
Digite o índice do grafo (0, 1, 2, ...): 0
~~~

## **2. Escolha do nó inicial e objetivo**

Após carregar o grafo, o sistema lista seus nós:
~~~
----- Escolha dentre os nós abaixo: -----
(0): CasaDaMamae
(1): ValeSeguro
(2): ColinaBranda
(3): PenhascoDoGavioes
(4): BosqueDoGuapardo
(5): CampoDoBode
(6): PlanicieH
(7): LagoLosPatos
(8): MontanhaAlta
(9): RetornoParaCasa

~~~

## **3. Agente – Planejamento e Execução**

O agente utiliza **A*** (A-Star) para buscar a rota mais eficiente entre os nós:
~~~
Plano traçado: ['CasaDaMamae', 'ValeSeguro', 'ColinaBranda', 'CampoDoBode', 'PlanicieH', 'LagoLosPatos', 'RetornoParaCasa']
~~~

Depois executa o plano:
~~~
Caminho planejado: ['CasaDaMamae', 'ValeSeguro', 'ColinaBranda', 'CampoDoBode', 'PlanicieH', 'LagoLosPatos', 'RetornoParaCasa']
Posição atualizada para: ValeSeguro
Posição atualizada para: ColinaBranda
Posição atualizada para: CampoDoBode
Posição atualizada para: PlanicieH
Posição atualizada para: LagoLosPatos
Posição atualizada para: RetornoParaCasa

Objetivo atingido!
~~~

## **4. Plotagem do Grafo**

Após a execução, o sistema exibe:

* os nós
* suas posições
* as arestas


## **Componentes do Sistema**

### 📘 **graphModel.py**

Responsável por:

* criar a estrutura interna do grafo
* armazenar posições e custos
* carregar grafo via JSON
* converter para NetworkX

### 📘 **algorithms_search.py**

Implementa:

* heurística (distância euclidiana)
* algoritmo A* via NetworkX

### 🤖 **agent.py**

O agente:

* percebe o ambiente
* planeja o caminho usando A*
* executa o plano passo a passo

### 🖥️ **main.py**

Gerencia:

* menu de seleção
* carregamento do grafo
* seleção dos nós
* execução do agente
* plotagem final

Integrantes da Equipe


| Nome              | Responsabilidade                                       |
| ----------------- | ------------------------------------------------------ |
| **Rafael**  | Modelagem do grafo, criação de JSONs, documentação |
| **Carlos**  | Implementação do algoritmo A*                        |
| **Marcelo** | Agente, integração, menu e visualização do grafo   |



## **Conclusão**

Este projeto demonstra o funcionamento de agentes baseados em objetivos usando grafos.

Foi implementado:

* leitura de grafos via JSON
* planejamento com A*
* execução automática
* visualização integrada
* interação via menu

É um exemplo completo e funcional de IA aplicada à navegação.
