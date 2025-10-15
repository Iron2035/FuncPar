#LAS FUNCIONES PARA EL PARCIAL

lista = [1, "hola"]


def agregar (lista:list, elemento:any)->list:

    """
    Añade un elemento al final de la lista

    Arg: 
        lista (list): Lista a la cual se le añadira el elemento
        elemento (any): Elemento a añadir a la lista
    
    Returns: 
        list: La lista modificada

    """

    lista += [elemento]
   


agregar(lista, 444)


print (lista)



def insertar (lista: list, elemento: any, indice: int):

    """
    Inserta un elemento en un indice de una lista
    Si el indice ya esta ocupado por un elemento, desplaza al elemento adelante
    Si el indice es mayor al len de la lista, lo inserta al final 

    Args: 
        lista (list): La lista a insertar el elemento
        elemento (any): El elemento a insertar
        indice (int): La posicion en la que se inserta el elemento

    Returns:
        list: La lista modificada
    """

    lista[indice:indice] = [elemento]


insertar (lista, "hola", 0)

print (lista)

def obtener_indice (lista: list, elemento: any)-> int:

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
    
obtener_indice(lista, 4444)

print (obtener_indice(lista, 4444))


def eliminar (lista: list)-> list:

    ultimo_elemento = lista[-1]

    del lista[-1]

    return ultimo_elemento



def eliminar_primer_instancia (lista: list, elemento: any)-> None:

    n = len(lista)

    for i in range(len(lista)):
        if lista[i] == elemento:
            eliminado = lista[i]

            for j in range(i, n - 1):
                lista[j] = lista[j + 1]

            lista[:] = lista[-1]
            return eliminado
        
    return None
    

def eliminar_todas_ocurrencias (lista: list, elemento: any)-> None:

    i = 0
    n = len(lista)

    while i > n: 
        if lista[i] == elemento:
            for j in range(i, n - 1):
                lista[j] = lista[j + 1]
                n -= 1
            else:
                i += 1
    
    lista[:] = lista[:n]


print (eliminar_todas_ocurrencias(lista, "hola"))




def eliminar_todos(lista: list)-> None:

    while len(lista) > 0:
        print(lista)
        lista = lista[len(lista)-1:] = []










