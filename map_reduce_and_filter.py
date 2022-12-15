# Gestión de un restaurante de comida rápida
# Supongamos que mientras te preparas para entrar en le mercado de la programación, te contratan para llevar un restaurante de comida rápida. El producto final es una hamburguesa y lleva los siguientes ingredientes:

# pan
# loncha de tomate
# loncha de pepinillo
# loncha de cebolla
# carne
# Es decir, cada producto final es la combinación de 5 ingredientes, cada uno de los cuales tiene que ser procesado previamente. Como sabes programación, el problema de cómo optimizar la producción de hamburguesas está chupado.

# Preparas 6 mesas. Cinco para los ingredientes y una final. Cada mesa está atendida por un empleado.

# Mesa del pan: hay una lista de panes que el empleado transforma en una lista de panes cortados por la mitad.
# Mesa del tomate: lista de tomates que el empleado transforma en una lista de lonchas
# Mesa del pepinillo: lista de pepinillos que el empleado transforma en una lista de lonchas
# Mesa de la cebolla: lista de cebollas que el empleado transforma en una lista de lonchas
# Mesa de la carne: una lista de bolas de carne molida que el empleado da forma y prepara a la plancha y transforma en una lista... ya lo habrás pillado. ;-)
# En la última mesa, el empleado hace lo siguiente: va pillando un ingrediente de cada una de las otras mesas, y ensambla, o reduce (lo pillas, ¿verdad?) esos 5 ingredientes, a 1 hamburguesa lista. Su resultado final es una lista de hamburguesas.

# Cada una de las 5 primeras mesas es una lista que se transforma en otra (ingrediantes crudos -> ingredientes preparados). El empleado correspondiente, se pasea por la mesa, produciendo la nueva lista.

# La mesa final es una lista de ingredientes finales. El empleado va a cada una de las mess de ingredientes, pilla uno, y forma (en su mesa) una lista de ingredientes preparados. Luego se mueve por la mesa, reduciendo esos ingredientes al producto final.

# Puntos Importantes
# Ya te habrás dado cuenta que hemso puesto en práctica nuestros conocimientos de computación para crear la maquinaria perfecta para producir hambuguesas. Algunas cosas qu ehay que destacar:

# Las mesas map pre-procesan los ingredientes / datos
# La mesa reduce aprovecha el trabajo hecho por las map y combina sus resultados en un producto final.
# Algo muy imporante que tal vez no hayas visto, pero que es clave para la eficiencia del sistema es el siguiente:

# Las mesas NO dependen la una de la otra

# Esto quiere decir que:

# Mientras no se queden sin ingredientes, el que corta el pan no tiene que esperar que el del tomate termine, etc...
# Mientras no se queden sin ingredientes, se pueden producir pequeños atrasos en una mesa sin que el sistema pare. Es decir, el de lso pepinillos puede ir a mear sin que se pare todo (hay suficientes penillos cortados en la lista de pepinillos cortados como para aguantar un poco)
# Cada mesa puede ser atendida por personas diferentes
# Esas personas, mientras cada una haga su trabajo, no necesitan comunicarse ni ponerse de acuerdo en nada.





# Ejemplo con Código
# Te contratan en una empresa que vende pantuflas calefactadas por usb para programadores. Las ventas mensuales vienen desglosadas por divisa (se vende en USD, EUR, GBP y JPI) . 
# Todo ello viene en una lista, cuyos elementos son listas con las ventas en dichas divisas y en ese orden:

# sales = [[2300, 345, 1949, 2222, 5939], [5252, 7886, 6363, 4432, 6653], [6262626, 47774, 72727, 636363], [363636, 4828, 199333, 7264]]
# [total_end_usd, total_en_euro, toal_enlibras, total_enyen]

# Transfórmalo en una venta de totales, usando tu propio map, reduce y filter

def my_filter(elements, predicate):
    """
    recibe una lista y un predicado. devuelve otra lista con aquellos elementos
    que superan el test del predicado
    """
    accum = [] 
    for element in elements:
        if predicate(element):
            accum.append(element)
    return accum

def my_map(seq,transformer):
    new_seq = []
    for element in seq:
        new_seq.append(transformer(element))
    return new_seq

def my_reduce(seq, initial_value, combinator):
    """
    Recorre una lista llamada seq y va combinando los valores mediante un 
    combinador (que no sabemos muy bien qué es, pero que se recibe como parámetro. 
    Devuelve el valor reducido o combinado de todos los elementos de la lista.
    """
    accum = initial_value
    for element in seq:
        accum = combinator(accum, element) 
    return accum

def make_sub_totals(list_of_sales):
    """
    devuelve una lista con los totales en su propia divisa
    """
    return my_map(list_of_sales, lambda list_of_nums : my_reduce(list_of_nums, 0, lambda a, b: a + b))
        

def convert_to_usd(subtotals, rates):
    """
    Convierte un lista de USD, EUR, GBP, JYI a partir de una lista de tasas de conversion
    """
    values_in_usd = []
    # Recorro la lista de totales
    for index, sub_total in enumerate(subtotals):# enumerate recibe una lista y te devuelve la posicion del elemento y el elemento
        # multiplico cada uno por su tasas de conversión correspondiente y lo guardo en la nueva lista
        values_in_usd.append(sub_total * rates[index])
        
    return values_in_usd

    
def grand_total_usd(sales):
    """
    Devuelve un total en USD
    """
    return my_reduce(sales, 0, lambda a, b: a + b)