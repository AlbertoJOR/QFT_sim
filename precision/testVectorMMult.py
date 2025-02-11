import random
import math
import util as u 
import carith as ca

def random_complex():
    """Genera un número complejo aleatorio con partes reales e imaginarias en [-1,1]"""
    real = random.uniform(-1, 1)
    imag = random.uniform(-1, 1)
    return (real, imag)

def complex_norm(vector):
    """Calcula la norma euclidiana de un vector de números complejos"""
    return math.sqrt(sum(r**2 + i**2 for r, i in vector))

def normalize_complex_vector(size):
    """Genera un vector aleatorio de números complejos con norma 1"""
    vector = [random_complex() for _ in range(size)]
    norm = complex_norm(vector)
    return [(r / norm, i / norm) for r, i in vector]

def random_complex_matrix(size):
    """Genera una matriz cuadrada aleatoria de números complejos de tamaño (size x size)"""
    return [[random_complex() for _ in range(size)] for _ in range(size)]

def complex_mult(c1, c2):
    """Multiplica dos números complejos representados como tuplas (real, imag)"""
    real1, imag1 = c1
    real2, imag2 = c2
    return (real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2)

def matrix_vector_mult(matrix, vector):
    """Multiplica una matriz cuadrada compleja por un vector complejo"""
    size = len(matrix)
    result = [(0, 0)] * size  # Vector resultado inicializado en ceros

    for i in range(size):
        sum_real, sum_imag = 0, 0  # Suma acumulada de la fila
        for j in range(size):
            real, imag = complex_mult(matrix[i][j], vector[j])  # Multiplicación compleja
            sum_real += real
            sum_imag += imag
        result[i] = (sum_real, sum_imag)  # Almacena el resultado en el vector

    return result

def print_complex_vector(vector):
    """Imprime un vector de números complejos de manera legible"""
    for r, i in vector:
        print(f"({r:.5f} {i:+.5f}i)")
    print()

def print_complex_matrix(matrix):
    """Imprime una matriz de números complejos de manera legible"""
    for row in matrix:
        print(" ".join(f"({r:.5f} {i:+.5f}i)" for r, i in row))
    print()

# Tamaño del vector y matriz
n = 3  # Puedes cambiarlo

# Generar vector normalizado y matriz cuadrada aleatoria
vector = normalize_complex_vector(n)
matrix = random_complex_matrix(n)

# Multiplicación matriz * vector
result = matrix_vector_mult(matrix, vector)

# Imprimir resultados
print("Vector complejo normalizado:")
print_complex_vector(vector)

print("Matriz cuadrada compleja aleatoria:")
print_complex_matrix(matrix)

print("Resultado de Matriz × Vector:")
print_complex_vector(result)

FRACTION_W = 12
vectorFixed = ca.complexVectorToFixed(vector, FRACTION_W)
matrixFixed =  ca.complexMatrixToFixed(matrix, FRACTION_W)

print("Resultado fixed")
resultFixed = ca.ComplexFixedVectorMatrixMult(vectorFixed, matrixFixed, FRACTION_W, FRACTION_W+2)
u.printComplexFixedVector(resultFixed, FRACTION_W+2, FRACTION_W)

