# Importy
import numpy as np
import time

# Stałe

# Wartości początkowe
x_0 = 1
x_1:np.longdouble = 1/30

# Wspłóczynniki w zależności rekurencyjnej
a = 30
b = -10
c = 30
d = 0

# Wartość parametru k
k = 900

# Typy zmiennych
types = [np.single, np.double, np.longdouble]

# Funkcje

def lab1(x_k_1, x_k, k, k_max, type):
    for type in types:

        # Rekurencja w przód
        start = time.time()
        result1 = rekurencjaPrzod(x_k_1, x_k, k, k_max, type)
        end = time.time()
        print("Funckja: ", rekurencjaPrzod.__name__)
        print("Typ: ", type)
        print("Czas wykonania: ", end - start)
        print("Wartość: ", result1)
        print("------------------------------------")

        # Rekurencja w tył
        start = time.time()
        result2 = rekurencjaTyl(result1[0], result1[1], k_max, type)
        end = time.time()
        print("Funckja: ", rekurencjaTyl.__name__)
        print("Typ: ", type)
        print("Czas wykonania: ", end - start)
        print("Wartość: ", result2)
        print("------------------------------------")

# Funkcja do rekurencji w przód
def rekurencjaPrzod(x_k_1, x_k, k, k_max, type) -> type[2]:
    result = type((-b*x_k - a*x_k_1)/c)
    # print([x_k, result])
    if k == k_max:
        return [x_k, result]
    else:
        return rekurencjaPrzod(x_k, result, k+1, k_max, type)

# Funkcja do rekurencji w tył
def rekurencjaTyl(x_k_1, x_k, k, type) -> type[2]:
    result = type((-b*x_k_1 - c*x_k)/a)
    # print([result, x_k_1])
    if k == 2:
        return [result, x_k_1]
    else:
        return rekurencjaTyl(result, x_k_1, k-1, type)


# Wywołanie głównej funkcji
lab1(x_0, x_1, 2, k, types[1])