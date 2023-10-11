def listar_tareas(inventario):
    #Valido si hay tareas en el inventario
    if not inventario:
        print("No hay tareas registradas\n")
    else:
        print("\nLista de tareas")
        
        for indice, tarea in enumerate(inventario):
            print(indice,". -",tarea["titulo"], "descripcion", tarea["descripcion"])