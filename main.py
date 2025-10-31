import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  # 👈 importa o matplotlib

class GoalBasedAgent:
    def __init__(self, environment, start, goal):
        self.env = environment      # grafo do ambiente
        self.current = start        # estado atual
        self.goal = goal            # objetivo
        self.path = []              # caminho planejado

    def perceive(self):
        """Percebe os vizinhos do estado atual."""
        return list(self.env.neighbors(self.current))

    def plan(self):
        """Planeja o caminho até o objetivo usando o menor trajeto."""
        try:
            self.path = nx.shortest_path(self.env, self.current, self.goal)
            print("Plano traçado:", self.path)
        except nx.NetworkXNoPath:
            print("Nenhum caminho disponível até o objetivo!")

    def act(self):
        """Executa a próxima ação do plano."""
        if self.path and self.current != self.goal:
            self.path.pop(0)
            if self.path:
                self.current = self.path[0]
                print(f"Movendo-se para {self.current}")
        else:
            print("Objetivo atingido!")

# ======= Ambiente =======
env = nx.Graph()
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('C', 'D'),
    ('D', 'E')
]
env.add_edges_from(edges)

# ======= Agente =======
agent = GoalBasedAgent(env, start='A', goal='E')
agent.plan()

# ======= Execução =======
while agent.current != agent.goal:
    agent.act()

# ======= Visualização do grafo =======
# Define o layout para posicionar os nós
pos = nx.spring_layout(env, seed=42)

# Desenha o grafo
nx.draw(
    env,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=1200,
    font_size=14,
    font_weight='bold',
    edge_color="gray"
)

# Mostra o caminho percorrido pelo agente
if agent.path:
    path_edges = list(zip(agent.path, agent.path[1:]))
    nx.draw_networkx_edges(env, pos, edgelist=path_edges, edge_color='red', width=2.5)

plt.title("Mapa de Rotas do Agente Baseado em Objetivo")
plt.show()
