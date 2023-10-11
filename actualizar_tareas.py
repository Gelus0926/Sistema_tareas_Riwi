from listar_tareas import *

def actualizar_tareas(inventario):
    listar_tareas(inventario)
    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice de la tarea a actualizar: "))
            if(indice < 0 or indice > len(inventario)):
                print("El indice no existe en la lista.")
            else: 

                titulo = input("Ingrese el nuevo nombre de la tarea: ")
                descripcion = input("Ingrese la nueva descripcion de la tarea: ")
                print("Actualizando el producto",inventario[indice]["titulo"])

                inventario[indice]["titulo"] = titulo
                inventario[indice]["descripcion"] = descripcion

                print("\nEl producto fue actualizado con exito!\n")

        except:
            print("Oops!, algo salió mal")