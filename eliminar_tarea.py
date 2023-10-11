from listar_tareas import *

def eliminar_tarea(inventario):
    listar_tareas(inventario)

    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice de la tarea a eliminar: "))
            if(indice < 0 or indice > len(inventario)):
                print("El indice no corresponde a ninguna tarea\n")
            else:
                print("Eliminando tarea ...")
                inventario.pop(indice)
                print("La tarea fue eliminado con éxito.\n")
        except:
            print("Oops!, algo salió mal")
