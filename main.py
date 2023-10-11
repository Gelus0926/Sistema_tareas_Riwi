from agregar_tareas import *
from listar_tareas import *
from actualizar_tareas import *
from eliminar_tarea import *
from mostrar_menu import *

def main():
    inventario = []
    while True:
        
        mostrarMenu()
        opcion = input("Ingrese una opción: ")

        if(opcion == "1"):
            listar_tareas(inventario)

        elif(opcion == "2"):
            agregar_tareas(inventario)
        
        elif(opcion == "3"):
            actualizar_tareas(inventario)

        elif(opcion == "4"):
            eliminar_tarea(inventario)
            
        elif(opcion == "5"):
            break
        

main()