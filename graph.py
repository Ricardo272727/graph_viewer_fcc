import fcc
from vertex import Vertex
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

    """
        CAMBIOS HECHOS EN 19/01/20
        CAMBIOS REALIZADOS (marcados en *):
            1. Se le agrega un diccionario a la fila, el cual tendra una plantilla de la siguiente forma:
                edges = {'amount': 1, 'weight': 1}
            temporalmente la cantidad sera de 1
            2. Se reemplaza el valor "1" por la variable "edges" para ser ingresada dentro de la matriz de adyacencia
    """
    def add_vertex(self, v, conexions):
        """ anade un vertice 'v' a la lista self.vertex
        y conecta el vertice con los vertices especificados en conexions
        llena la matriz de adyacencia
        """
        range = [0, self.mat_size+1]

        # expandir la matriz de adyacencia
        self.expand_matrix()

        # fila y columna en la matriz de adyacencia
        v.adj_mat_pos = self.mat_size - 1

        """
            ADICION DE RALEX: BORRAR CUANDO SEA ACEPTADO
        """
        edges = {'amount': 1, 'weight': 1}                          # * "edges" variable created
        for con in conexions:
            if fcc.validate_range(con, range):
                self.mat_adj[self.mat_size-1][con] = edges
                self.mat_adj[con][self.mat_size-1] = edges
        # agregar nuevo vertice a la lista de vertices
        self.vertex.append(v)

    """
        CAMBIOS REALIZADOS:
        CAMBIOS HECHOS EN 17/01/20
            1. statment "not" agregado en la condicional del rango
            2. se realiza un decremento del tamanio de la matriz al final del metodo
            3. agregados comentarios como "posible" solucion al problema de las posiciones de los vertices
        
        CAMBIOS HECHOS EN 19/01/20
            1. "v_id" reemplazado por "v_pos"
    """    
    def delete_vertex(self, v_pos):
        """ Elimina el vertice con la pos
        (posicion en la matriz de adyacencia) : v_pos"""
        # wachar si la pos esta en rango
        if not fcc.validate_range(v_pos, [0, self.mat_size]):
            return False

        # quitar la columna y fila del vertice en la matriz de adyacencia
        for row in self.mat_adj:
            # elimina de la fila el elemento en el indice v_id
            row.pop(v_pos)

        self.mat_adj.pop(v_pos)

        # eliminar de la lista de vertices 
        for v in self.vertex:
            if v.adj_mat_pos == v_pos:
                self.vertex.remove(v)
                self.vertex[v_pos].adj_mat_pos -= 1      # Decrementa la posicion del vertice "recolocado" para no perderlo
            if v.adj_mat_pos > v_pos:
                v.adj_mat_pos -= 1     # Decrementa la posicion del vertice. De cierta forma, se "recorren"

        # decrementar el tamanio de la matriz cuadrada super perfecta y espectacularmente brillante
        # el man de arriba se mamut                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.mat_size -= 1
    
    """
        CAMBIOS HECHOS EN 19/01/20
        CAMBIOS REALIZADOS (marcados en *):
            1. Se le agrega un diccionario a la fila, el cual tendra una plantilla de la siguiente forma:
                edges = {'amount': 0, 'weight': 1}
            2. Se reemplaza el valor "0" por la variable "edges" para ser ingresada dentro de la matriz de adyacencia
    """
    def expand_matrix(self):
        """
        expande la matriz de adyacencia una columna y una fila
        """
        self.mat_size += 1
        # anade una columna a la matriz
        """
            ADICION DE RALEX: BORRAR CUANDO SEA ACEPTADO
        """
        edges = {'amount': 0, 'weight': 1}                          # * "edges" variable created
        for row in self.mat_adj:
            row.append(edges)                                       # * "edges" replacing "0" to be appended instead
        # crea una fila de 0's y la anade al final de la matriz
        new_row = [edges for x in range(self.mat_size)]             # * "edges" replacing "0" to be appended instead
        self.mat_adj.append(new_row)


    def show_adj_matrix(self):
        """
        hace la mostracion de la matriz
        """
        for row in self.mat_adj:
            print(row)
        # Lo siento xDDD si sabes como imprimirlo mejor pues me dices juasjuas

    def show_vertex(self):
        # muestra la lista de vertices con estilo
        for v in self.vertex:
            m = "\nUniversal id -> " + str(v.get_id()) 
            m += "\nLabel -> " + v.label
            m += "\nColor -> " + str(v.color) 
            m += "\nAdyacency matrix position -> " + str(v.adj_mat_pos)         
            print(m)

def main():
    g = Graph()

    info = {"A": 0xff0000, "B" : 0x4F6CFF, "C": 0xFF5396, "D" : 0xFFFF00,
    "E": 0xFFFF00 , "F": 0x00FFFF, "G": 0x008080, "H": 0x000080 }

    count = 0
    for label, color in info.items():
        # anade un nuevo vertice, y lo conecta a todos los vertices existentes
        g.add_vertex(Vertex(label=label, color=color), [x for x in range(count)])
        count += 1

    print("Adj mat: ")
    g.show_adj_matrix()

    print("Vertices: ")
    g.show_vertex()

    g.delete_vertex(3)
    g.delete_vertex(4)

    print("\nMatriz de adyacencia: ")
    g.show_adj_matrix()

    print("\nVeritces: ")
    g.show_vertex()

    g.add_vertex(Vertex("\\Lambda", 64), [1,3,5,7])

    print("\nMatriz de adyacencia: ")
    g.show_adj_matrix()

    print("\nVeritces: ")
    g.show_vertex()

main()