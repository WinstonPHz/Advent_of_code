import heapq
from functools import cache
from copy import deepcopy
import math
import random

class d24():
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.singles = {}
        self.all_nodes = []

    def get_crosses(self, set_a, set_b):
        total_cross = 0
        crossed = set()
        # Check set a
        for node in set_a:
            connections = self.nodes[node]
            for con in connections:
                pair = [node, con]
                pair.sort
                if con in set_b:
                    if tuple(pair) not in crossed:
                        crossed.add(tuple(pair))
        return len(crossed)

    def kerlin_algorithm(self):
        # populate both sets first
        A = set()
        B = set()
        flipper = False
        for node_id in self.nodes:
            if flipper:
                A.add(node_id)
                flipper = False
            else:
                B.add(node_id)
                flipper = True
        old_cross_count = 10000
        while True:
            for swap in self.all_nodes:
                new_cross_count = self.get_crosses(A,B)
                if new_cross_count == 3:
                    print(self.nodes["cmg"])
                    print("Answer 1:", len(A)*len(B))
                    return
                if new_cross_count > old_cross_count:
                    print(f"Returning to old AB, {new_cross_count} {old_cross_count}")
                    A = old_A
                    B = old_B
                else:
                    old_cross_count = new_cross_count
                print(swap, old_cross_count, A, B)
                old_A = A
                old_B = B
                #random_int = random.randint(0, len(self.all_nodes)-1)
                #swap = self.all_nodes[random_int]
                if swap in A:
                    A.remove(swap)
                    B.add(swap)
                elif swap in B:
                    B.remove(swap)
                    A.add(swap)

    def add_node(self, line):
        key, connections = line.split(": ")
        if key not in self.nodes.keys():
            self.nodes[key] = []
        if key not in self.all_nodes:
            self.all_nodes.append(key)
        for connection in connections.split(" "):
            if connection not in self.all_nodes:
                self.all_nodes.append(connection)
            if connection not in self.nodes[key]:
                self.nodes[key].append(connection)
            if connection not in self.nodes.keys():
                self.nodes[connection] = []
            if key not in self.nodes[connection]:
                self.nodes[connection].append(key)



obj = d24()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_node(line)
obj.kerlin_algorithm()
