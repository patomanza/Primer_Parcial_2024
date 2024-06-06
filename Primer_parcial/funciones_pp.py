import random


def cargar_archivo(path:str):
    
    with open(path,"r",encoding= "utf-8") as archivo:
        lista_peliculas = []
        encabezado = archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
            
            id,titulo,genero,rating = linea
            
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = int(rating)
            
            lista_peliculas.append(pelicula)
    
    print("Datos guardados en coleccion\n")
    
    return lista_peliculas

def imprimir_lista(lista_peliculas):
    print(f"{'ID':^5}{'Título':^30}{'Género':^15}{'Rating':^10}")
    print("-" * 60)
    
    for pelicula in lista_peliculas:
        print(f"{pelicula['id']:^5}{pelicula['titulo']:^30}{pelicula['genero']:^15}{pelicula['rating']:^10}")

def generar_ratings(lista_peliculas):
    lista_ratings = []
    
    for pelicula in lista_peliculas:
        rating = round(random.uniform(1,10), 1)
        lista_ratings.append(rating)
    
    return lista_ratings


def mappeadora_ratings(lista_peliculas):
    ratings = generar_ratings(lista_peliculas)
    
    for pelicula in lista_peliculas:
        pelicula["rating"] = random.choice(ratings)
    
    return lista_peliculas

def generar_generos(lista_peliculas):
    generos = {1:"Drama", 2:"Comedia",3: "Accion",4: "Terror"}
    numero_genero = random.randint(1,4)
    
    lista_peliculas["genero"] = generos[numero_genero]
    
    return lista_peliculas


def mappeadora_generos(lista_peliculas):
    
    for pelicula in lista_peliculas:
        generar_generos(pelicula)
    
    return lista_peliculas


def solicitar_genero(mensaje:str):
    generos_validos = ["Drama","Comedia","Terror","Accion"]
    
    while True:
        genero_seleccionado = input(mensaje).capitalize()
        if genero_seleccionado in generos_validos:
            return genero_seleccionado
        else:
            print("Error,genero invalido. Seleccione alguno de los siguientes(Drama,Terror,Accion,Comedia)")

def filtrar_por_genero(lista_peliculas, genero):
    
    nombre_archivo = f"{genero.lower()}.csv"
    
    lista_filtrada = []
    
    for pelicula in lista_peliculas:
        if pelicula["genero"] == genero:
            lista_filtrada.append(pelicula)
    
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"{'ID':^5}{'Título':^30}{'Género':^15}{'Rating':^10}\n")
        
        for pelicula in lista_filtrada:
            linea = f"{pelicula['id']:^5}{pelicula['titulo']:^30}{pelicula['genero']:^15}{pelicula['rating']:^10}\n"
            archivo.write(linea)
    
    print(f"Se ha creado el archivo con nombre: {nombre_archivo}")


def ordenar_peliculas(lista_peliculas):
    #INCOMPLETO
    
    pass

def informar_mejor_rating(lista_peliculas):
    
    bandera_primero = True
    for pelicula in lista_peliculas:
        if bandera_primero == True or float(pelicula['rating']) > pelicula_maximo_rating:
            pelicula_maximo_rating = float(pelicula['rating'])
            bandera_primero = False
    
    for pelicula in lista_peliculas:
        if float(pelicula['rating']) == pelicula_maximo_rating:
            titulo = pelicula['titulo']
            rating_maximo = float(pelicula['rating'])
    
    
    print(f"{'Titulo':^30}|{'Rating':^10}")
    print(f"{titulo:<30}|{rating_maximo:>10.1f}")


def guardar_en_json():
    #INCOMPLETO
    pass

def validacion_entero(mensaje:str) -> int:
    """
    Brief: Solicita al usuario la entrada de un numero entero,
            y verifica que la entrada sea un numero y no una cadena de caracteres.
            Si el usuario ingresa letras u otros caracteres, 
            sigue solicitando la entrada hasta que sea un numero entero.

    Args:
        mensaje (str): Es un string que se utilizara como mensaje
                        para solicitar la entrada del usuario.

    Returns:
        int: Retorna el numero entero ingresado por el usuario,
                solo si representa un numero entero.
    """
    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            print("Error, ha ingresado letras. Ingrese solo numeros.")
        else:
            try:
                x = int(entrada)
                return x
            except ValueError:
                print("Por favor, ingrese un número válido: ")