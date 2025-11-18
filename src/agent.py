import networkx as nx;


class agent:
    def __init__(self, graph, actual, objective):
        self.graph = graph;
        self.actual = actual;
        self.objective = objective;