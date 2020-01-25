

"""
Escribe un mensaje en el archivo:
graph_viewer.log
"""
def write_log(message):
    try:
        with open("graph_viewer.log", "a") as f_obj:
            f_obj.write("\n"+message)
            f_obj.close()
    except FileNotFoundError:
        pass

