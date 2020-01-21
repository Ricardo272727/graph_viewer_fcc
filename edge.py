class Edge():

    __universal_id = 0

    def __init__(self, label = "Edge", weight = 1):
        self.__id = Edge.__universal_id
        self.label = label
        self.weight = weight
        # self.color = 0x0 # Not sure to include it
        Edge.__universal_id += 1
        self.vertex_1 = None
        self.vertex_2 = None

    def get_id(self):
        return self.__id

    def set_vertexes(self, vertex_1, vertex_2):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2

    def is_incident_with(self, vertex):
        return vertex == self.vertex_1 or vertex == self.vertex_2