"""
This is a library to build applications with graphs 

Created by: 

Ricardo Alejandro Segura Cuanalo (Rick)
Alejandro Batres Pedroza (Rrrralex)

Students of Computer Science in the FCC
"""

# valida si un numero esta en un rango range[0] <= x < range[1]
def validate_range(x, range):
    if(type(range) is list and len(range) == 2):
        if(range[0] <= x and x < range[1]):
            return True
    return False