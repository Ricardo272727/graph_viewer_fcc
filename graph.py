
import json
import math
import sys

class Edge():
    def __init__(self, v1, v2, weight=0):
        self.begin = v1
        self.end = v2
        self.weight = weight

class Vertex():
    def __init__(self, value, index, color='blue'):
        
        self.value = value
        self.index = index
        self.color = color


class Graph():
    """ 
    Class graph with a adyacency matrix
    """
    def __init__(self):
        self.vertices = []
        self.matrix = []
        self.edges = []
        
    def add_vertex(self, vertex = None):
        n = len(self.matrix)
        if vertex is None:
            vertex = Vertex(0, n)
        self.vertices.append(vertex)
        
        if n == 0:
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
                self.edges.append(Edge(begin, end))
                return True
        return False
    
    def dijsktra(self, source):
        dist = [sys.maxsize] * self.vertices
        dist[source] = 0
        visited = [False] * self.vertices
        
        for index in range(self.vertices):
            
            u = self.minDistance(dist, visited)
            
            
            
        
    
    def show(self):
        for row in self.matrix:
            print(row)
        print(self.vertices)
        print(self.edges)


    def load_graph(self, filename):
        try:
            with open(filename, 'r') as file:
                self.matrix.clear()
                self.vertices.clear()
                self.edges.clear()
                content = json.load(file)
                for row in content["matrix"]:
                    self.matrix.append(row)
                for v in content["vertices"]:
                    newVertex = Vertex(v['value'], v['index'], v['color'])
                    self.vertices.append(newVertex)
                for e in content["edges"]:
                    newEdge = Edge(e['begin'], e['end'], e['weight'])
                    self.edges.append(newEdge)
                return True
        except FileNotFoundError:
            return False

    def save_graph(self, filename):
        try:
            with open(filename, 'w') as file:
                content = {}
                content["matrix"] = self.matrix
                content['vertices'] = []
                content['edges'] = []
                for v in self.vertices:
                    vertex = {'color': v.color, 'value': v.value, 'index': v.index }
                    content['vertices'].append(vertex)
                for e in self.edges:
                    edge = {'begin': e.begin, 'end': e.end, 'weight': e.weight }
                    content['edges'].append(edge)
                content = json.dumps(content, indent=4)
                file.write(content)
                file.close()
                return True
        except FileNotFoundError:
            return False

    
