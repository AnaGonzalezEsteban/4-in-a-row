# Funciones para:
# 1. Detectar la presencia de una instancia del elemento dentro de una lista, en cualquier posición
# 2. Detectar la presencia de N instancias dentro de una lista, en cualquier posición
# 3. Detectar la presencia de N elementos seguidos dentro de una lista


# 1. Detectar la presencia de una instancia del elemento dentro de una lista, en cualquier posición. Función optimizada más adelante.
# def find_one(list,needle):
#     """Devuelve True si encuentra a needle en la lista en alguna posición.
#     Si no, devuelve False"""
#     # inicializo el contador y el booleano que indica si se cumple o no la condicion
#     found = False
#     index=0
#     # Recorrro la lista  mientras no encuentre la aguja
#     while not found and index < len(list):
#         # compruebo si el elemento actual es la aguja
#         if needle == list[index]:
#             # si lo es, he terminado y devuelvo True
#             found = True
#             # Si termino la lista y no lo he encontrado, devuelvo False.
#         else:
#             found = False
#         #avanzamos al sigiente elemento
#         index = index + 1
#     #devolvemos el resultado guardado en found
#     return found


        
# Comprobaciones:
# print(find_one([1,2,3,4,5],4))
# print(find_one([1,2,3,4,5],0))
# print(find_one([],4))
# print(find_one([1,2,3],'c'))
# print(find_one(['a','b'],42))


# # 1. Detectar la presencia de una instancia del elemento dentro de una lista, en cualquier posición(con not_found cambiada)
# def not_find_one(list,needle):
#     """Devuelve True si NO encuentra a needle en la lista en alguna posición.
#     Si lo encuentra, devuelve False"""
#     # inicializo el contador y el booleano que indica si se cumple o no la condicion
#     not_found = True
#     index=0
#     # Recorrro la lista  mientras no encuentre la aguja
#     while not_found and index < len(list):
#         # compruebo si el elemento actual es la aguja
#         if needle == list[index]:
#             # si lo es, he terminado y devuelvo True
#             not_found = False
#             # Si termino la lista y no lo he encontrado, devuelvo False.
#         else:
#             not_found = True
#         #avanzamos al sigiente elemento
#         index = index + 1
#     #devolvemos el resultado guardado en found
#     return not_found

# # Comprobaciones:
# print(not_find_one([1,2,3,4,5],4))
# print(not_find_one([1,2,3,4,5],0))
# print(not_find_one([],4))



# 2. Detectar la presencia de N instancias dentro de una lista, en cualquier posición. Sin correcciones.
# def find_n(list,needle,n):
#     # inicializo el contador de evces que lo he encontrado
#     count=0
#     # inicializo el indice del elemento actual
#     index=0
#     # mientras no haya encontrado n veces y no haya terminado la lista
#     while count < n and index < len(list): 
#         # si la encuentro, actualizo el contador
#         if needle == list[index]:
#             count += 1
#         #pase lo que pase, actualizo el indice
#         index +=1
#     # devuelvo el resultado de comparar n con el contador
#     return count >= n

# # Comprobaciones
# print(find_n([1,2,3,4, 3, 3], 3, 2))
# print(find_n([1,2,3,4, 3, 3], 3, 0))
# print(find_n([1,2,3,4, 3, 3], 3, -12))


# 2. Detectar la presencia de N instancias dentro de una lista, en cualquier posición. Con correcciones para n=0 y n<0 hecho por mí:
# def find_n(list,needle,n):
#     # inicializo el contador de evces que lo he encontrado
#     count=0
#     # inicializo el indice del elemento actual
#     index=0
#     #Si n=0 y el elemento sí está en la lista, devuelve False
#     if n==0 and needle in list:
#         return False
#     elif n==0 and needle not in list:
#         return True
#     # Si n es menor que 0, indica que n no puede ser negativo y devuelve False.
#     elif n<0:
#         print('n no puede tomar valores negativos')
#         return False
#     # Si n es mayor que 0:
#     elif n>0:
#         # mientras no haya encontrado n veces y no haya terminado la lista
#         while count < n and index < len(list): 
#             # si la encuentro, actualizo el contador
#             if needle == list[index]:
#                 count += 1
#             #pase lo que pase, actualizo el indice
#             index +=1
#         # devuelvo el resultado de comparar n con el contador
#         return count >= n

# Comprobaciones
# print(find_n([1,2,3,4, 3, 3], 3, 2))
# print(find_n([1,2,3,4, 3, 3], 2,3))
# print(find_n([1,2,3,4, 3, 3], 3, 0))
# print(find_n([1,2,3,4, 3, 3], 7, 0))
# print(find_n([1,2,3,4, 3, 3], 3, -12))


# 2. Detectar la presencia de N instancias dentro de una lista, en cualquier posición. Errores corregidos por el profesor:
def find_n(list,needle,n):
    if n>0:
        # inicializo el contador de evces que lo he encontrado
        count=0
        # inicializo el indice del elemento actual
        index=0
        # mientras no haya encontrado n veces y no haya terminado la lista
        while count < n and index < len(list): 
            # si la encuentro, actualizo el contador
            if needle == list[index]:
                count += 1
            #pase lo que pase, actualizo el indice
            index +=1
        # devuelvo el resultado de comparar n con el contador
        return count >= n
    
    else:
        return False

# Comprobaciones
# print(find_n([1,2,3,4, 3, 3], 3, 2))
# print(find_n([1,2,3,4, 3, 3], 3, 0))
# print(find_n([1,2,3,4, 3, 3], 3, -12))


# 1. Detectar la presencia de una instancia del elemento dentro de una lista, en cualquier posición.
# Habiendo resuelto el problema de find_n, resulta repetitivo tener una función find_one que repita todo el proceso. 
# Basta con que find_one devuelva el resultado de apicar find_n a una única búsqueda:
def find_one(list,needle):
    """Devuelve True si encuentra a needle en la lista en alguna posición.
    Si no, devuelve False"""
    return find_n(list,needle,1) #revisar por que n is not defined. he puesto 1 en lugar de n porque quiere encontra 1 ocurrencia!!!


# 3. Detectar la presencia de N elementos seguidos dentro de una lista:
def find_streak(list,element,size): # Lo llamamos distinto porque lo que buscamos ahora es una racha. Needle= un unico elemento, mientras que element=racha de elementos
    """
    Devuelve True si en list hay size o más elementos SEGUIDOS
    Devuelve False en caso contrario y también si size es <=0 (para obligar a que el tamaño sea siempre mayor que 0) TIENE UN ERROR HAY QUE CORREGIRLO,MIRAR SUS APUNTES
    """
    if size >0:
        # inicializo el contador de veces que lo he encontrado
        count=0
        # inicializo el indice del elemento actual
        index=0
        # inicializo el indicador de racha
        streak=False
        # mientras no haya encontrado a size elements seguidos y la lista no se haya terminado
        while count<size and index<len(list):
            # si lo encuentro, activo el indicador de rachas e incremento el contador
            if list[index]==element:
                streak=True
                count+=1
            # si no lo encuentro, desactivo el indicador de rachas y pongo el contador a cero de nuevo
            else:
                streak=False
                count=0
            # pase lo que pase, avanzo al siguiente elemento incrementando indice
            index+=1
            # SOLO SI ESTAMOS EN RACHA, devolvemos el resultado de comparar el contador con size
        if streak:
            return count>=size
        else:
            return False
    else:
        return False

# Comprobaciones:
# print(find_streak([1,2,5,5,5,3,4],5,3))
# print(find_streak([1,2,5,5,5,3,4],5,0))
# print(find_streak([1,2,5,5,5,3,4],5,-10))
# print(find_streak([1,2,5,5,3,4],5,3))
# print(find_streak([1,2,5,5,5,5,4],5,3))
# print(find_streak([1,2,3,3,3],3,3))


# Reescribir find_n como caso especial de find_streak si se puede


def first_elements(list_of_lists):
    """Recibe una matriz(lista de listas) y devuelve una lista con los primeros elementos de cada una de las lsitas de la matriz"""
    result=[]
    for sub_list in list_of_lists:
        result.append(sub_list[0])
    return result
    # return nth_elements(list_of_lists,0)

# Comprobaciones:
# print(first_elements([[1,2,3],[1,2,3],[3,2,1]]))

def nth_elements(list_of_lists,n):
    """Recibe una matriz(lista de listas) y devuelve una lista con los enesimos elementos de cada una de las lsitas de la matriz"""
    result=[]
    for sub_list in list_of_lists:
        result.append(sub_list[n])
    return result

# Comprobaciones:
# matrix=[[1,2,3,4],[4,3,2,1],[0,0,0,0],[9,9,9,9]]
# print(nth_elements(matrix,0))

def transpose(list_of_lists):
    """Recibe una matriz y devuelve su transpuesta"""
    #creo una matriz vacía en la que iré acumulando
    transp=[]
    #desde cero al ultimo indice de list_of_lists
    for index,sub_list in enumerate(list_of_lists):#enumerate devuelve indice  elemento al recorrer la lista 
        #esta fila es equivalente a: for index in range(len(list_of_lists)):
    #extraigo sus valores enesimos y se los encasqueto a la acumulada
        transp.append(nth_elements(list_of_lists,index))
    #devuelvo la acumulada
    return transp

# print(matrix==transpose(transpose(matrix)))
# print(transpose(matrix))

# def displace(elements,n):
#     """Recibe una lista y la desplaza un elemento a la derecha. Lo que sobra al final se borra y el espacio del principio se rellena con None
#     [1,2,3,4]-->[None,1,2,3]"""
#     if n ==0:
#         return elements
#     else:
#         res=elements
#         filler=[None]*n
#         res=filler+res #insert no devuelve copia de una lista, sino que altera una lista existente
#         return res[:-n]


def displace(elements,n):
    """Recibe una lista y la desplaza un elemento a la derecha si n es positivo y hacia la izquierda si n es negativo. 
    Lo que sobra al final se borra y el espacio del principio se rellena con None
    [1,2,3,4]-->[None,1,2,3]"""
    res=elements
    filler=[None]*abs(n)
    if n ==0:
        return elements
    elif n>0:
        res=filler+res #si lo quiero hacer con insert, no devuelve copia de una lista, sino que altera una lista existente
        return res[:-n]
    else:
        res=res+filler
        return res[abs(n):]


def displace_matrix(matrix):
    """Desplaza cada una de las listas de la matriz su índice -1"""
    #creo una matri vacia que ire construyendo
    d=[]
    #por cada columna de la matriz original. la desplazo indice -1
    for i in range(len(matrix)):
        #añado la columna desplaza a la amtriz que estoy construyendo
        d.append(displace(matrix[i],i-1))
    #devuelvo la matriz que he construido
    return d


def replace(elements,predicate,new_value): # prima hermana de filter
    """REcibe una lista, un predicado y un valor por el que queremos sustituir. Todo elemento que cumpla el predicado será sustituido con el elemento nuevo"""
    #creamos un acumulador
    new_list=[]
    #recorro la lista original
    for element in elements:
        #si un elemento pasa el test, lo cambio por el nuevo
        if predicate(element):
            new_list.append(new_value)
        #si no, se queda tal cual:
        else:
            new_list.append(element)
    #devuelvo el acumulador:
    return new_list


def replace_matrix(matrix,predicate,new_element): 
    """Aplica replace a todas las listas de una matriz y te devuelve una matriz"""
    accum=[]
    for sublist in matrix:
        accum.append(replace(sublist,predicate,new_element))
    return accum


# invertir listas y matrices:
def reverse_list(l):
    return list(reversed(l))


def reverse_matrix(matrix):
    accum=[]
    for sublist in matrix:
        accum.append(reverse_list(sublist))
    return accum

