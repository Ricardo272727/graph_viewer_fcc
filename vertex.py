class Vertex():

    __universal_id = 0

    def __init__(self, label = "Vertex", color = 0x0):
        self.__id = Vertex.__universal_id
        self.label = label
        self.color = color
        Vertex.__universal_id += 1
        self.adj_mat_pos = -1

    def get_id(self):
        return self.__id