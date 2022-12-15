def convert(prices,rate):
    """Crea una función que recibe una lista de precios en dolares
    Devuelve esos mismo precios en otra divisa.
    Para ello también recibe una tasa de conversión"""
    new_prices=[]
    for price in prices:
        new_prices.append(price*rate)
    return new_prices
    
# print(convert([1,2,3,4],1.1))   


def convert_if_big(prices,rate): 
    """Funcion que recibe la misma lista de precios en dolares y solo convierte a otra divisa los que sean mayores que 10"""
    new_prices=[]
    for price in prices:
        if price >10:
            new_prices.append(price*rate)
        else:
            new_prices.append(price)
    return new_prices

# def convert_if_big_(prices,rate): #OTRA ALTERNATIVA
#     """Funcion que recibe la misma lista de precios en dolares y solo convierte a otra divisa los que sean mayores que 10"""
#     new_prices=[]
#     for price in prices:
#         new_price=price
#         if price >10:
#             new_price=price*rate
#         new_prices.append(new_price)
#     return new_prices

# print(convert_if_big([1,34,10,12],2.5))
# print(convert_if_big_([1,34,10,12],2.5))

    
def to_euro_string(prices):
    """funcion que recibe una lista de numeros con precios en euros y devuelve una lsita de cadenas.
    Cada precio debe de ser convertido en una cadena con el estandar ISO para €: 45 = EUR 45"""
    lista_iso=[]
    for element in prices:
        lista_iso.append('EUR '+str(element))
    return lista_iso

# print(to_euro_string([34,54,0.55]))

# Se está repitiendo un patrón:
# Todas estas funciones crean una lista vacía, cogen una lista existente, le hacen una operación y el resultado lo meten en la lista nueva.
# Esta nueva lista tiene la misma longitud que la antigua


def map(seq,transformer): #transformer es una funcion que transforma los elementos de la lista
    new_seq=[]
    for element in seq:
        new_seq.append(transformer(element))
    return new_seq

# print(map([1,2,3,4],lambda x:x+1))
# print(map([1,2,3,4],lambda x:str(x)))
# print(map([1,2,3,4],lambda x:x*2 if (x%2==0) else x)) # COMO PONER IF EN UNA FUNCION LAMBDA!!!!!!!!!!!! desglosado con las funciones a continuación:


def is_even(n): #para saber si un  numero es par
    return (n%2)==0

# print(is_even(6))
# print(is_even(3))

def dupl_if_even(n):
    if is_even(n):
        return n*2
    else:
        return n

# print(map([1,2,3,4],dupl_if_even))

# lista_de_listas=[[],[1,2,3],[None],[True,'10']]
# print(map(lista_de_listas,len))




def stringify(seq):
    """Usando map, define la función stringify, que recibe una lista de cosas, y devuelve una lista de esas cosas convertidas en cadenas. 
Por ejemplo: [1, 4, True, None] ---> ['1', '4', 'True', 'None']
Recuerda, map es una forma de divide y vencerás. Ya no te tienes que preocupar de cómo procesar toda la lista, sólo de cómo transformar un elemento en una cadena."""
    return map(seq,lambda x: str(x))

# print(stringify([1, 4, True, None]))



def ucase(seq):
    """Usando map, crea una función ucase que recibe una lista de cadenas y devuelve una lista de cadenas, todas en mayúsculas"""
    return map(seq,lambda x: x.upper())
    
# print(ucase(['uno','dos','tres','cuatro']))

def to_positive(seq):
    """Usando map, crea la función to_positive que recibe una cadena de números positivo sy negativos, y devuelve una lista con los valores absolutos de dichos números."""
    return map(seq,lambda x: x if x>=0 else -x)

# print(to_positive([1,-1,2,-2,3,-3]))



def dollar_only(seq):
    """Usando map crea la función dollar_only. Recibe una lista de valores en diferentes divisas (usando el estandar ISO), tales como:
    'CHF 12' Doce francos suizos
    'USD 22' Veintidós dólares
    'EUR 60' 60 euros
    y devuelve una lista, de igual longitud, donde sólo aparezcan los valores que estaban en dólares. Los demás se sustituyen por la cadena vacía:
    ['CHF 23', 'EUR 87', 'USD 2', 'USD 21', 'BTC 3'] ---> ['', '', 'USD 2', 'USD 21', '']"""
    def transf(word):
        result=''
        if word[0]=='U' and word[1]=='S' and word[2]=='D':
            result=word
        return result
    return map(seq,transf)

# print(dollar_only(['CHF 23', 'EUR 87', 'USD 2', 'USD 21', 'BTC 3'] ))


def lens(list_of_lists):
    """Usando map, crea la función lens. lens recibe una lista de listas y devuelve una lista con las longitudes de dichas listas"""
    return map(list_of_lists,lambda list: len(list))

# print(lens([[1],[1,None],[1,None,True],[1,None,True,'Ana'],[1,None,True,'Ana',[]]]))

