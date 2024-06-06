from funciones_pp import * 


menu = ["\n1.Cargar archivo","2.Imprimir lista","3.Asignar rating","4.Asignar genero","5.Filtrar por genero",
        "6. Ordenar peliculas","7. Informar mejor rating","8.Guardar peliculas","9.Salir\n"]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

seguir = True
selecciono_1 = False

while seguir == True:
    
    mostrar_menu()
    
    opcion = validacion_entero("Ingrese una opcion: ")
    if opcion < 0 or opcion > 8:
        print("Error ingrese una opcion valida\n")
    
    
    match opcion:
        case 1:
            peliculas = cargar_archivo("Primer_parcial/movies.csv")
            selecciono_1 = True
        case 2:
            if not selecciono_1:
                print("Error, primero debes cargar el archivo.\n")
            else:
                imprimir_lista(peliculas)
        case 3:
            if not selecciono_1:
                print("Error, primero debes cargar el archivo.\n")
            else:
                mappeadora_ratings(peliculas)
        case 4:
            if not selecciono_1:
                print("Error, primero debes cargar el archivo.\n")
            else:
                mappeadora_generos(peliculas)
        case 5:
            if not selecciono_1:
                print("Error, primero debes cargar el archivo.\n")
            else:
                genero = solicitar_genero("Seleccione un genero para filtrar (Drama,Accion,Terror,Comedia): ")
                filtrar_por_genero(peliculas,genero)
        case 6:
            if not selecciono_1:
                print("Error, primero debes cargar el archivo.\n")
            else:
                pass
        case 7:
            if not selecciono_1:
                print("Error, primero debes cargar el archivo.\n")
            else:
                informar_mejor_rating(peliculas)
        case 8:
            seguir = False


