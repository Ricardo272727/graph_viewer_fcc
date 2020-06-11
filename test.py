
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
    
    def test_load_file(self):
        self.assertTrue(self.graph.load_graph("example_file.json"))
        self.graph.show()
        self.graph.add_edge(1,1)
        self.assertTrue(self.graph.save_graph("example_file_result.json"))
        self.graph.show()
        
if __name__ == '__main__':
    unittest.main()