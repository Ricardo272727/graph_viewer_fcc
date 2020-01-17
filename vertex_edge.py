class Vertex():

    __universal_id = 0

    def __init__(self, label = "Vertex", color = 0x0):
        self.__id = Vertex.__universal_id
        self.label = label
        self.color = color
        Vertex.__universal_id += 1

    def get_id(self):
        return self.__id

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

def Test():

    v1 = Vertex()
    print("Vertex 1 ID: "+str(v1.get_id()))
    v2 = Vertex()
    print("Vertex 2 ID: "+str(v2.get_id()))
    # print(v.__id) This doesn't work 'cause it's a private attribute!!

    e1 = Edge()
    print("Edge 1 ID: "+str(e1.get_id()))
    e2 = Edge()
    print("Edge 2 ID: "+str(e2.get_id()))

Test() # This executes the instructions provided inside the Test method