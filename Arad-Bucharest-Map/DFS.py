#    Copyright 2019 Atikur Rahman Chitholian
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from collections import deque

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def depth_first_search(self, start, goal):
      print('Depth first =:')
      found, fringe, visited, came_from = False, deque([(0, start)]), set([start]), {start: None}
      print('{:11s} | {:23s} | {}'.format('Node to be Visited', 'Node Visited', 'Time'))
      print("----------------------------------------------------------")
      print('{:11s} | {:23s} | {}'.format('-', start, 0))
      while not found and len(fringe):
          start = time.time()
          depth, current = fringe.pop()
          print('{:11s}'.format(current), end=' | ')
          if current == goal: found = True; break
          for node in self.neighbors(current):
              if node not in visited:
                  visited.add(node); fringe.append((depth + 1, node))
                  came_from[node] = current
          print(', '.join([n for _, n in fringe]), end='')
          stop = time.time()
          print(" | ", round(stop-start, 7))
      if found: print(); return came_from
      else: print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else:
          print('[', end= '')
        print(goal, end=', ');return

    def __str__(self):
        return str(self.edges)


graph = Graph(directed=False)
romaniaMap = {
    ('Arad','Zerind'),
    ('Arad','Sibiu'),
    ('Arad','Timisoara'),
    ('Zerind','Oradea'),
    ('Oradea','Sibiu'),
    ('Timisoara','Lugoj'),
    ('Sibiu','Fagaras'),
    ('Sibiu','Rimnicu Vilcea'),
    ('Lugoj','Mehadia'),
    ('Fagaras','Bucharest'),
    ('Rimnicu Vilcea','Pitesti'),
    ('Rimnicu Vilcea','Craiova'),
    ('Mehadia','Dobreta'),
    ('Bucharest','Pitesti'),
    ('Bucharest','Urziceni'),
    ('Bucharest','Giurglu'),
    ('Pitesti','Craiova'),
    ('Craiova','Dobreta'),
    ('Urziceni','Hirsova'),
    ('Urziceni','Vaslui'),
    ('Hirsova','Eforie'),
    ('Vaslui','Lasi'),
    ('Lasi','Neamt'),
}
for edge in romaniaMap:
  graph.add_edge(*edge[:])
start, goal= 'Arad', 'Bucharest'
firstStart = time.time()
traced_path = graph.depth_first_search(start, goal)
print()
if (traced_path): print ("\nBest route from Arad to Bucharest is:"); Graph.print_path(traced_path, goal);print(']')
firstStop = time.time()
print("The time it takes to find the path is: ", round(firstStop-firstStart, 5))
