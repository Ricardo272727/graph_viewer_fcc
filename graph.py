

import fcc

"""
Objetivos de aqui a dos semanas
agregar nodo ia
eliminar 
conectar
mostrar mat
crear nuevo arbol/grafo
arrastrar y crear nodo
"""

class Graph():
    """ Clase grafo con lista de vertices y una matriz
    de adyacencia """
    def __init__(self):
        self.vertex = []
        self.mat_adj = []
        self.mat_size = 0

    def add_vertex(self, v, conexions):
        """ anade un vertice 'v' a la lista self.vertex
        y conecta el vertice con los vertices especificados en conexions
        llena la matriz de adyacencia
        """
        range = [0, self.mat_size+1]

        # expandir la matriz de adyacencia
        self.expand_matrix()

        for con in conexions:
            if fcc.validate_range(con, range):
                self.mat_adj[self.mat_size-1][con] = 1
                self.mat_adj[con][self.mat_size-1] = 1
        # agregar nuevo vertice a la lista de vertices
        self.vertex.append(v)
        
    def delete_vertex(self, v_id):
        """ Elimina el vertice con el id 
        (posicion en la matriz de adyacencia) : v_id"""
        # wachar si el id esta en rango
        if fcc.validate_range(v_id, [0, self.mat_size]):
            return False

        # quitar la columna y fila del vertice en la matriz de adyacencia
        for row in self.mat_adj:
            # elimina de la fila el elemento en el indice v_id
            row.pop(v_id)

        self.mat_adj.pop(v_id)

        # eliminar de la lista de vertices 
        for v in self.vertex:
            if v.id == v_id:
                self.vertex.remove(v)
                break
        
    
    def expand_matrix(self):
        """
        expande la matriz de adyacencia una columna y una fila
        """
        self.mat_size += 1
        # anade una columna a la matriz
        for row in self.mat_adj:
            row.append(0)
        # crea una fila de 0's y la anade al final de la matriz
        new_row = [0 for x in range(self.mat_size)]
        self.mat_adj.append(new_row)


    def show_adj_matrix(self):
        """
        hace la mostracion de la matriz
        """
        for row in self.mat_adj:
                print(row)

def main():
    g = Graph()
    g.add_vertex(27, [])
    g.add_vertex(28, [0, 1])
    g.add_vertex(29, [0,1,2])
    g.show_adj_matrix()

main()