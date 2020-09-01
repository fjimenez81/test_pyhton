from math import factorial


def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

def numero_combinaciones(m, n):
    """Calcula y devuelve el número de combinaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // (factorial(n) * factorial(m - n))

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]


def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])

def permutaciones(c, n):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
               [])

def numero_permutaciones(m, n):
    """Calcula y devuelve el número de permutaciones
       posibles que se pueden hacer con m elementos
       tomando n elementos a la vez.
    """
    return factorial(m) // factorial(m - n)


print(imprime_ordenado(permuta([123,1,-1,12,-12,2,-2,23,-23,3,-3,34,-34,4,-4,45,-45,5,-5,56,-56,6,-6,67,-67,7,-7,78,-78,8,-8,89,-89,9,-9])))