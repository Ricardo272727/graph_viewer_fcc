
import json


class Vertex():
    def __init__(self, value, index, weight=0, label="-"):
        self.label = label
        self.value = value
        self.weight = weight
        self.index = index
        
class Graph():
    """ 
    Class graph with a adyacency matrix
    """
    def __init__(self):
        self.vertices = []
        self.matrix = []
        
    def add_vertex(self, vertex = None):
        n = len(self.matrix)
        if vertex is None:
            vertex = Vertex(0, n)
            
        self.vertices.append(vertex)
        
        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            for row in self.matrix:
                row.append(0)
            new_row = [0 for i in range(n+1)]
            self.matrix.append(new_row)
    
    
    def add_edge(self, begin, end):
        n = len(self.matrix)
        if begin >= 0 and begin < n and end >= 0 and end < n:
                self.matrix[begin][end] = 1
                return True
        return False
    
    def dijsktra(self, v1, v2):
        print("Implement me!")
    
    def show(self):
        for row in self.matrix:
            print(row)
        print(self.vertices)


    def load_graph(self, filename):
        try:
            with open(filename, 'r') as file:
                self.matrix.clear()
                self.vertices.clear()
                content = json.load(file)
                for row in content["matrix"]:
                    self.matrix.append(row)
                for v in content["vertices"]:
                    self.vertices.append(v)
                return True
        except FileNotFoundError:
            return False

    def save_graph(self, filename):
        try:
            with open(filename, 'w') as file:
                content = {}
                content["matrix"] = self.matrix
                content["vertices"] = self.vertices
                content = json.dumps(content, indent=4)
                file.write(content)
                file.close()
                return True
        except FileNotFoundError:
            return False

    
