
import pickle


class Vertex():
    def __init__(self, value):
        self.value = value
        self.weight = 0
        
class Graph():
    """ 
    Class graph with a adyacency matrix
    """
    def __init__(self):
        self.vertices = []
        self.matrix = []
        
    def add_vertex(self, vertex = None):
        if vertex is None:
            vertex = Vertex('-')
            
        self.vertices.append(vertex)
        
        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            for row in self.matrix:
                row.append(0)
            new_row = [0 for i in range(len(self.matrix)+1)]
            self.matrix.append(new_row)
    
    
    def add_edge(self):
        print("Comming soon")
   
    
    def show(self):
        for row in self.matrix:
            print(row)
        

    def show_adj_matrix(self):
        """
        hace la mostracion de la matriz
        """
        for row in self.mat_adj:
            string_row = ''
            for edges in row:
                string_row += '[ {} ]'.format(len(edges))
            print(string_row)


    def save_graph(self, filename):
        """
        Guarda este objeto en un archivo binario
        filename: /ruta/del/archivo/sin/extension/.bin
        """
        try:
            with open(filename + ".bin", 'wb') as file_obj:
                pickle.dump(self, file_obj)
                file_obj.close()
                return True
        except FileNotFoundError:
            return False

    def load_graph(self, filename):
        try:
            with open(filename + ".bin", 'rb') as file_obj:
                content = pickle.loads(file_obj.read())
                return content
        except FileNotFoundError:
            return None

