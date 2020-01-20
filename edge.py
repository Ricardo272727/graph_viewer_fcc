"""
    POSIBLEMENTE SEA DESECHADO
"""
class Edge():

    __universal_id = 0

    def __init__(self, label = "Edge", weight = 1):
        self.__id = Edge.__universal_id
        self.label = label
        self.weight = weight
        # self.color = 0x0 # Not sure to include it
        Edge.__universal_id += 1

    def get_id(self):
        return self.__id