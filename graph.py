import fcc
from vertex import Vertex
from edge import Edge 
from debug_options import write_log 
import json
import pickle

"""
Objetivos de aqui a dos semanas
agregar nodo ->yes
eliminar ->yes
conectar ->yes
mostrar mat ->yes
crear nuevo arbol/grafo ->no
arrastrar y crear nodo ->no 
"""

class Graph():
    """ Clase grafo con lista de vertices y una matriz
    de adyacencia """
    def __init__(self):
        self.vertexes = []
        self.edge = []
        self.mat_adj = []
        self.mat_size = 0

    def vertex_by_ID(self, vertex_id):
        for vertex in self.vertexes:
            if vertex.get_id() == vertex_id:
                return vertex
        return None

    def vertex_by_position(self, vertex_position):
        for vertex in self.vertexes:
            if vertex.adj_mat_pos == vertex_position:
                return vertex
        return None
    
    def validate_vertex(self, vertex):
        for v in self.vertexes:
            if v.get_id() == vertex.get_id():
                return False
        return True

    def validate_edge(self, edge):
        for edge_list in self.edge:
            if edge_list.get_id() == edge.get_id():
                return False
        return True

    def add_vertex(self, vertex = None):
        if vertex is None:
            vertex = Vertex()

        if not self.validate_vertex(vertex):
            return False
        
        # expandir la matriz de adyacencia
        self.expand_matrix()

        # fila y columna en la matriz de adyacencia
        vertex.adj_mat_pos = self.mat_size - 1
        self.vertexes.append(vertex)
   
    def delete_vertex(self, vertex):
        if self.mat_size <= 0 or vertex is None:
            return False
        
        if not vertex in self.vertexes:
            return False
        
        # quitar las aristas incidentes al vertice en caso de que exista alguna
        for edge in self.edge:
            if edge.is_incident_with(vertex):
                self.delete_edge(edge)

        vertex_pos = vertex.adj_mat_pos
        # quitar la columna y fila del vertice en la matriz de adyacencia
        for row in self.mat_adj:
            # elimina de la fila el elemento en el indice v_id
            row.pop(vertex_pos)

        self.mat_adj.pop(vertex_pos)

        # eliminar de la lista de vertices 
        for matrix_vertex in self.vertexes:
            if matrix_vertex.adj_mat_pos == vertex_pos:
                self.vertexes.remove(matrix_vertex)
                self.vertexes[vertex_pos].adj_mat_pos -= 1      # Decrementa la posicion del vertice "recolocado" para no perderlo
            if matrix_vertex.adj_mat_pos > vertex_pos:
                matrix_vertex.adj_mat_pos -= 1     # Decrementa la posicion del vertice. De cierta forma, se "recorren"

        # decrementar el tamanio de la matriz cuadrada super perfecta y espectacularmente brillante
        # el man de arriba se mamut                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.mat_size -= 1
        return True

    def add_edge(self, vertex_1, vertex_2, edge = None):
        if vertex_1 is None or vertex_2 is None:
            return False

        if edge is None:
            edge = Edge()
        
        if not self.validate_edge(edge):
            return False
        
        edge.set_vertexes(vertex_1, vertex_2)
        self.mat_adj[vertex_1.adj_mat_pos][vertex_2.adj_mat_pos].append(edge)
        if vertex_1 != vertex_2:
            self.mat_adj[vertex_2.adj_mat_pos][vertex_1.adj_mat_pos].append(edge)
        self.edge.append(edge)
        return True

    def delete_edge(self, edge):
        if self.mat_size <= 0 or edge is None:
            return False

        if not edge in self.edge:
            return False

        list_1 = self.mat_adj[edge.vertex_1.adj_mat_pos][edge.vertex_2.adj_mat_pos]
        if edge.vertex_1 != edge.vertex_2:
            list_2 = self.mat_adj[edge.vertex_2.adj_mat_pos][edge.vertex_1.adj_mat_pos]

        list_1.remove(edge)
        if edge.vertex_1 != edge.vertex_2:
            list_2.remove(edge)
        self.edge.remove(edge)
        return True

    def expand_matrix(self):
        """
        expande la matriz de adyacencia una columna y una fila
        """
        self.mat_size += 1
        # anade una columna a la matriz
        for row in self.mat_adj:
            edges = []
            row.append(edges)                                           # *
        # crea una fila de 0's y la anade al final de la matriz
        new_row = [[] for x in range(self.mat_size)]                 # *
        self.mat_adj.append(new_row)

    def show(self):
        print("Adj mat: ")
        self.show_adj_matrix()
        self.show_vertex()
        self.show_edge()

    def show_adj_matrix(self):
        """
        hace la mostracion de la matriz
        """
        for row in self.mat_adj:
            string_row = ''
            for edges in row:
                string_row += '[ {} ]'.format(len(edges))
            print(string_row)

    def show_vertex(self):
        for v in self.vertexes:
            m = 'Vertex: [ID: {}, Label: {}, Color: {}, Position: {}]'.format(v.get_id(), v.label, v.color, v.adj_mat_pos)
            """
            m = "\nUniversal id -> " + str(v.get_id()) 
            m += "\nLabel -> " + v.label
            m += "\nColor -> " + str(v.color) 
            m += "\nAdyacency matrix position -> " + str(v.adj_mat_pos)         
            """
            print(m)

    def show_edge(self):
        for e in self.edge:
            m = 'Edge: [ID: {}, Label: {}, Weight: {}]'.format(e.get_id(), e.label, e.weight)
            print(m)

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
            write_log("File not found " + filename + ".bin")
            return None

def main():
    g = Graph()

    v1 = Vertex("A")
    v2 = Vertex("B")

    g.add_vertex(v1)
    g.add_vertex(v2)

    g.show_vertex()
    print("\nMatriz con dos vertices")
    g.show_adj_matrix()

    e1 = Edge("e1")
    e2 = Edge("e2")
    e3 = Edge("e3")
    e4 = Edge("e4")

    g.add_edge(v1,v2,e1)
    g.add_edge(v1,v1,e2)
    g.add_edge(v2,v2,e3)
    g.add_edge(v2,v2,e4)

    print()
    g.show_edge()
    print("\nMatriz con 4 aristas (tres siendo un bucle)")
    g.show_adj_matrix()

    g.delete_edge(e2)

    print("Matriz sin una arista (bucle)")
    g.show_adj_matrix()

    g.delete_vertex(v1)
    
    
    g.show_vertex()
    print("\nMatriz sin el vertice 1")
    g.show_adj_matrix()

    print(g.save_graph("example_file"))
    n = g.load_graph("example_file")
    
    n.show()
    

main()