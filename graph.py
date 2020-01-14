

def main():
    g = Graph()
    g.add_vertex(27, [0, 0])
    g.add_vertex(27, [1, 1])
    g.add_vertex(27, [1, 2])
    g.add_vertex(27, [3, 2])
    g.show_adj_matrix()

def validate_range(x, range):
    if(type(range) is list and len(range) == 2):
        if(range[0] <= x and x < range[1]):
            return True
    return False

class Vertex():
    def __init__(self, value):
        self.val = value
        self.id = value

    def value(self, v):
        self.val = v


class Graph():
    """ Clase grafo con lista de vertices y una matriz
    de adyacencia """
    def __init__(self):
        self.vertex = []
        self.mat_adj = []
        self.mat_size = 0

    def add_vertex(self, v, coords):
        if len(coords) == 2:
            range = [0, self.mat_size+1]
            
            if validate_range(coords[0], range) and validate_range(coords[1], range):
                self.expand_matrix()
                self.mat_adj[coords[0]][coords[1]] = 1
                self.mat_adj[coords[1]][coords[0]] = 1
                

    def expand_matrix(self):
        self.mat_size += 1

        for row in self.mat_adj:
            row.append(0)

        new_row = [0 for x in range(self.mat_size)]
        self.mat_adj.append(new_row)


    def show_adj_matrix(self):
        for row in self.mat_adj:
                print(row)

main()