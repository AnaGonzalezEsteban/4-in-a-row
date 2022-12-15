
from itertools import accumulate


class Coin:
    def __init__(self,amount):
        self.amount=amount
        
class Switch:
    def __init__(self,state):
        self.state=state


def sum_all(numbers):
    """recibe una suma de números y loscombina mediante +  a uno solo, que será el total"""
    total_so_far=0
    for element in numbers:
        total_so_far+=element
    return total_so_far

# def sum_all_w(numbers):
#     """recibe una suma de números y loscombina mediante +  a uno solo, que será el total"""
#     total_so_far=0
#     index=0
#     while index< len(numbers):
#         total_so_far+=numbers[index]
#         index+=1
#     return total_so_far

def mult_all(numbers):
    """recibe una suma de números y la reduce a uno solo usando la multiplicación"""
    total_so_far=1
    for element in numbers:
        total_so_far*=element
    return total_so_far

# def mult_all(numbers):
#     """recibe una suma de números y la reduce a uno solo usando la multiplicación"""
#     total_so_far=1
#     index=0
#     while index< len(numbers):
#         total_so_far*=numbers[index]
#         index+=1
#     return total_so_far

def concat_all(strings):
    """Recibe una lista de cadenas y las reduce a una sola concatenandolas"""
    total_so_far=''
    for element in strings:
        total_so_far += element # + se aplica a las cadenas para concatenar
    return total_so_far

def and_all(bools):
    """ Reduce una lista de booleanos a uno solo usando and """
    total_so_far=True
    for element in bools:
        total_so_far = total_so_far and element
    return total_so_far

def or_all(bools):
    """ Reduce una lista de booleanos a uno solo usando and """
    total_so_far=False
    for element in bools:
        total_so_far = total_so_far or element
    return total_so_far

# print(and_all([True,True,True,False])) 
# print(and_all([Switch(False).state,Switch(False).state]))

def lengthf(seq):
    """Crea la función length() que recibe una lista y devuelve su longitud. 
    Ya sé que existe en Python una función len() que hace lo mismo. No la uses, quiero que crees la tuya propia.
    El bucle se puede hacer tanto con un for como con un while. Hazlo de las dos formas (lenghtf con for y lengthw con un while). Comprueba que ambos funcionan.
    Recuerda siempre probar con casos límite. Por ejemplo, ¿cual debería de ser el valor de: length([])?
    """
    # crea una variable donde acumular el tamaño
    size=0
    # recorre la lista `seq` y ve sumando 1 al acumulador por cada elemento
    for element in seq:
        size+=1
    # devuelve lo acumulado
    return size




# MUY IMPORTANTE SABER ESTO DE RECORRER LISTAS CON WHILE!!!!!!!!!!!!!!!!!!
# def lengthw(seq):
#     size=0
#     while size < len(seq): 
#         size+=1
#     return size

# def lengthw(seq): #VERSION DE FERNANDO, CON DOS INDICES PRO SI TUVIERAMOS QUE ITERAR DE DOS EN DOS O ALGO ASI
    #donde empiezo
    #donde termino
    #como paso de uno a otro
#     index=0
#     count=0
#     while index < len(seq): 
#          index+=1
#          count+=1
#      return count



def is_memberw(needle, seq):
    """
    Recibe dos parámetros, el primero es el que se busca y el segundo es la secuencia (lista) en
    la cual creemos que está. Devuelve True si needle está en la secuencia
    """
    found = False #indica si lo hemos encontrado o no
    index = 0     #contador para recorrer la lista
    while index < len(seq):
        # compara needle con el elemento
        if seq[index]==needle:
            # actualiza el elemento
            found=True
            index+=1
            break
        else:
            found=False
            index+=1
    return found


def is_memberf(needle, seq):
    """
    Recibe dos parámetros, el primero es el que se busca y el segundo es la secuencia (lista) en
    la cual creemos que está. Devuelve True si needle está en la secuencia
    """
    found = False #indica si lo hemos encontrado o no
    index = 0     #contador para recorrer la lista
    for element in seq:
        # compara needle con el elemento
        if seq[index]==needle:
            # actualiza el elemento
            found=True
            index+=1
            break
        else:
            found=False
            index+=1
    return found


def is_not_member(needle, seq):
    """is_not_member es el predicado opuesto a is_member: cuando is_member devuelve True, is_not_member devuelve False y vice versa. 
    Es decir, is_not_member es un predicado que determina si needle no es parte de la lista.
    Implementa is_not_member haciendo uso de is_member. Recuerda, DRY: do not repeat yourself"""
    return not is_member(needle, seq)


def how_many(needle, seq):
    """La función how_many recibe dos parámetros: lo que buscamos (la aguja) y una lista. Debe de devolver la cantidad de veces que la aguja aparece en la lista.
    how_many(4, ['lucas', 'grijander']) => 0
    how_many(42, [None, [], [42], 42]) => 1
    how_many(42, [42, 42, '42']) => 2
    Hazlo con un for y luego con un while.
    how_many es una función que recibe una secuencia o lista de valores y devuelve uno solo, que no es un booleano."""
    index=0
    for element in seq:
        if element == needle:
            index+=1
    return index


def reduce(seq, initial_value, combinator): #combinator es la función de la operación que quiero realizar
    """
    Recorre una lista llamada seq y va combinando los valores mediante un combinador (que no sabemos muy bien qué es, pero que se recibe como parámetro. 
    Devuelve el valor reducido o combinado de todos los elementos de la lista.
    """
    accum = initial_value
    for element in seq:
        accum = combinator(accum,element)
    return accum

# def sum(a,b):
#     return a+b

# def prod(a,b):
#     return a*b

# nums=[1,2,3,4,5,6,7,8,9]
# print(reduce(nums,0,sum))
# print(reduce(nums,1,prod))
# # print(reduce(nums,0,a+b)) Da error porque hay que meter una FUNCION
# print(reduce(nums,0, lambda a,b:a+b)) #también valdría meter una lambda
# print(reduce(nums,1, lambda a,b:a*b))
# print(reduce(['EUR3','USD44','CHF23'],'',lambda x,y:x+','+y))
