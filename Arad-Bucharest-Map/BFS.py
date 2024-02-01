# BFS GRAPH
from queue import Queue
import time

romaniaMap = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


def bfs(startingNode, destinationNode):
  print("Breadth First Search=: ")
  firstStart = time.time()
  # For keeping track of what we have visited
  visited = {}
  # keep track of distance
  distance = {}
  # parent node of specific graph
  parent = {}

  bfs_traversal_output = []
  # BFS is queue based so using 'Queue' from python built-in
  queue = Queue()

  # travelling the cities in map
  for city in romaniaMap.keys():
      # since intially no city is visited so there will be nothing in visited list
      visited[city] = False
      parent[city] = None
      distance[city] = -1

  # starting from 'Arad'
  startingCity = startingNode
  visited[startingCity] = True
  distance[startingCity] = 0
  queue.put(startingCity)
  print('{:11s} | {:23s} | {}'.format('Node to be Visited', 'Node Visited', 'Time'))
  print("----------------------------------------------------------")
  while not queue.empty():
    start = time.time()
    u = queue.get()     # first element of the queue, here it will be 'arad'
    bfs_traversal_output.append(u)
    print('{:18s}'.format(u), end=' | ')
    # explore the adjust cities adj to 'arad'
    for v in romaniaMap[u]:
      if not visited[v]:
        visited[v] = True
        print(v, end=',')
        parent[v] = u
        distance[v] = distance[u] + 1
        queue.put(v)
    stop = time.time()
    print(" | ", round(stop-start, 5))
      # reaching our destination city i.e 'bucharest'
  g = destinationNode
  path = []
  while g is not None:
      path.append(g)
      g = parent[g]
  print ("\nBest route from Arad to Bucharest is:")
  path.reverse()
  # printing the path to our destination city
  print(path)
  firstStop = time.time()
  print("The time it takes to find the path is: ", round(firstStop-firstStart, 5))


# Starting City & Destination City
bfs('Arad', 'Bucharest')
