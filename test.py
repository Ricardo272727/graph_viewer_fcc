
import unittest
from graph import Graph

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        
    def test_add(self):
        self.graph.add_vertex()
        self.assertEqual(len(self.graph.matrix), 1)
        self.graph.add_vertex()
        self.assertEqual(len(self.graph.matrix), 2)
        self.graph.show()
        
if __name__ == '__main__':
    unittest.main()