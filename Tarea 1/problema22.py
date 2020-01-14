import math
tupla1 = (0, 1)
tupla2 = (3, 5)
tupla3 = (7, 2)
tupla4 = (4, -2)


def isCuadrado(t1, t2, t3, t4):
    """
    Check if 4 dots form a square.

    Keyword arguments:
    t1 -- A dot coordinates in a 2D plane.
    t2 -- A dot coordinates in a 2D plane.
    t3 -- A dot coordinates in a 2D plane.
    t4 -- A dot coordinates in a 2D plane.
    """
    return getDistancia(t1, t2) == getDistancia(t2, t3) == getDistancia(t3, t4) == getDistancia(t4, t1)


def getDistancia(A, B):
    """
    Return the distance between 2 dots in a 2D plane.

    Keyword arguments:
    A -- A dot coordinates in a 2D plane.
    B -- A dot coordinates in a 2D plane.
    """
    return math.sqrt(((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2))


print(isCuadrado(tupla1, tupla2, tupla3, tupla4))
