import heapq
class Graph:
    def __init__(self):
      self.nodes = set()
      self.edfes = {}

    def add_node(self, value):
      self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
      if from_node not in self.edges:
        self.edges[from_node] = []
      self.edges[from_node].append((to_node,weight))

    def dijkstra(self, start):
      distance = {node: float('inf') for node in self.nodes}
      distance[start] = 0
      pq = [(0, start)]

      while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
          continue
        for neighbor, weight in self.edges.get(node, []):
          new_dist = dist + weight
          if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))
      return distance
