import random
import networkx as nx

nodes = set()
G = nx.DiGraph()

with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        key, connections = line.split(": ")
        nodes.add(key)
        for connection in connections.split(" "):
            nodes.add(connection)
            G.add_edge(key, connection, capacity=1.)
            G.add_edge(connection, key, capacity=1.)
cut_val = 1000

G.remove_edges_from(nx.minimum_edge_cut(G))
sum = 1
for a in nx.strongly_connected_components(G):
    print(a)
    sum *= len(a)
print(sum)
