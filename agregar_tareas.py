#Sistema de lista de tareas
def agregar_tareas(inventario):
    try: 
        titulo = input("Ingrese el titulo de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")

        tarea = {"titulo": titulo, "descripcion": descripcion}
        inventario.append(tarea)
        print("Se agregó la tarea con exito")
    except:
        print("Error al agregar la tarea")
