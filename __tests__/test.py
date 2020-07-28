
import unittest
from graph import Graph

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        
    
    def test_load_file(self):
        self.assertTrue(self.graph.load_graph("example_file.json"))
        
        self.assertTrue(self.graph.save_graph("example_file_result.json"))
        
        
if __name__ == '__main__':
    unittest.main()