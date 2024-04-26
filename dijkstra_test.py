import unittest
from dijkstra import Graph

class TestDijkstra(unittest.TestCase):
  def djikstra_test(self):
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('A', 'D', 5)
    g.add_edge('D', 'C', 1)

    distance = g.dijkstra('A')
    self.assertEqual(distance, {'A': 0, 'B': 1, 'C': 3, 'D': 5})

if __name__ == '__main__':
  unittest.main()
