def is_high_probability(probability):
    """
    Recibe una probabilidad (número entre 0 y 1.0) y devuelve
    True si dicha probabilidad está en el rango correcto y es alta (mayor o igual a 0.8)
    """
    if probability > 1 or probability < 0:
        result = False
    else:
        result = (probability >= 0.8)
    return result
        
# print(is_high_probability(7))
# print(is_high_probability(-4))
# print(is_high_probability(0.8))
# print(is_high_probability(0.9))
# print(is_high_probability(0.7))



def my_filter_for(elements, predicate):
    """
    recibe una lista y un predicado. devuelve otra lista con aquellos elementos
    que superan el test del predicado.
    Ejemplos de predicado:
        lambda x: x < 10`  Recibe un número y devuelve `True`si el número es menor que 10.
        lambda l: len(l) > 3` Recibe una lista y devuelve `True` si su longitud es mayor que 3 
    """
    accum = []#qué se va acumulando? cial es el valor inicial?
    for element in elements:
        if predicate(element):
            accum.append(element)
    return accum

def my_filter_while(elements, predicate):
    accum = []#qué se va acumulando? cial es el valor inicial?
    i=0
    while i < len(elements):
        if predicate(elements[i]):
            accum.append(elements[i])
        i+=1
    return accum

# print(my_filter_while([1,6,3,8,5,9],lambda x: x < 6))


def only_even(seq):
    return my_filter_for(seq,lambda x: x%2==0)

# print(only_even([1,2,3,4,5,6,7,8,9,11, 12,14,19,12]))


# NO ME FUNCIONAAAA!!! no se usar reduce para len!!!print(reduce(nums,0,lengthf)) me da error --- Se refiere a la suma total de los pares!!!!!! Por eso no me salía
from reduce import *
def total_even_in_list(seq):
    return reduce(only_even(seq),0,lambda a,b: a+b)

# print(total_even_in_list([1,2,3,4,5,6,7,8,9,11,12,14,19,12]))

def total_impares_in_list(seq):
    impares=my_filter_for(seq,lambda x: x%2!=0)
    return reduce(impares,0,lambda a,b: a+b)

# print(my_filter_for([1,2,3,4,5,6,7,8,9,11,12,14,19,12],lambda x: x%2!=0))
# print(total_impares_in_list([1,2,3,4,5,6,7,8,9,11,12,14,19,12]))



# Te contrataron en un banco como Data Analyst y tu primer trabajo es recibir una lista (larguísima) que contiene la probabilidad, 
# calculada mediante un modelo de ML, de que un cliente deje de pagar su hipoteca.
# Tu trabajo es quitarle esos muertos al banco, eliminando de la lista los que tengan una probabilidad inferior a un valor que te pasan.

import random

# lista de probabilidades (usando "list comprehensions")
probs = [random.random() for i in range(100) ]
# print(probs)

def remove_bad_customers(probabilities, threshold):
    """
    Recibe una lista de probabilidades de pago y un límite (threshold)
    Debe devolver una nueva lista con aquellas probabilidades que son iguales
    o mayores al threshold
    """
    return my_filter_for(probabilities,lambda x: x>=threshold) 


# print(remove_bad_customers([0,15,77,98,43,22,0.05],25))
print(remove_bad_customers(probs,0.7))



# Trabajas en un clínica de estética (en el departamento de IT, of course) y lo priemro que se le hace a los clientes es calcular su bmi.
# Tu trabajo es recibir una lista con dichos valores y crear una nueva con aquellos que están por debajo de 15 o por encima de 40. 
# En esos casos se supone que puede haberse producido un error,y se tiene que volver a calcular.

# Crea una función que devuelve una lista con esos valores extremos.
def is_extreme(bmi):
    extreme=False
    if bmi>40 or bmi<15:
        extreme=True
    return extreme


def extreme_bmis(list_of_bmis):
    """
    Recibe una lista y devuelve otra lista con los valores de bmi que se consideran
    sospechosos de ser un error por extremos (menor que 15 o mayor que 40)
    """
    return my_filter_for(list_of_bmis,is_extreme)



# Tienes una lista de "cosas", como por ejemplo la siguiente:

# [34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50']
# Tu trabajo es dejar pasar todo lo que no sea una lista.

# Para ello, primero averigua qué hace la función type de Python y asegúrate de entender las siguientes expresiones:
# type(34) - int
# type([3,4]) - list
# type([]) - list
# type([]) == int - False
# type([]) == list - True

# Ahora, crea la función lists_only que recibe una lista de "cosas" y devuelve una nueva lista con todo aquello que no era una lista, eliminado.
# lists_only([34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50']) devolverá  [ [3,4,5], [None, None], [], ['grijandermoney']]

def lists_only(seq):
    """Recibe una lista y saca de ella todo elemento que no sea una lista"""
    return my_filter_for(seq,lambda x: type(x)== list)

# print(lists_only([34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50']) )


# Usando la función lists_only, crea una función non_empty_lists que devuelve una lista con aquellos elementos que són listas y que además NO están vacías.
def non_empty_lists(seq):
    # return (my_filter_for(lists_only(seq), lambda x: len(x)>0)) # usando esta opcion recorres la lista dos veces
    return my_filter_for(seq, lambda x: (type(x)==list) and (len(x)>0)) # usando esto solo se recorre la lista una vez

print(non_empty_lists([34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50']))

# Para implementar non_empty_lists debes de llamar a lists_only.

# non_empty_lists([34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50'])
# devolverá

# [ [3,4,5], [None, None],  ['grijandermoney'], ]
