import time
import resource
from dijkstra import Graph

def memory_usage():
  return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024

def benchamrk():
  g = Graph()
  g.add_node('A')
  g.add_node('B')
  g.add_node('C')
  g.add_node('D')
  g.add_edge('A', 'B', 1)
  g.add_edge('B', 'C', 2)
  g.add_edge('A', 'D', 5)
  g.add_edge('D', 'C', 1)

  start_time = time.time()
  distance = g.dijkstra('A')
  end_time = time.time()

  print("Shortest distance:", distance)
  print("Execution time:", end_time - start_time, "seconds")
  print ("Memory usage:", memory_usage(), "KB")

if __name__ == "__main__":
  benchmark()
