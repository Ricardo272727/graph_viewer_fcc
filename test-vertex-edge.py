
from vertex import Vertex
from edge import Edge

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