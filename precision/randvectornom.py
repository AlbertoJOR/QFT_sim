import random
import math
import carith as ca
import util as u

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

def print_complex_vector(vector):
    """Imprime el vector complejo de forma legible"""
    for r, i in vector:
        print(f"({r:.5f} {i:+.5f}i)")
    print()

# Tamaño del vector
n = 4  # Puedes cambiarlo a cualquier valor

# Generar y normalizar el vector
vector = normalize_complex_vector(n)

# Imprimir el vector normalizado
print("Vector complejo normalizado:")
print_complex_vector(vector)

# Verificar la norma (debe ser aproximadamente 1)
norm_result = complex_norm(vector)
print(f"Norma del vector: {norm_result:.6f}")  # Debe ser ≈1

FRACTION_WIDTH = 12
fixed_vector = ca.complexVectorToFixed(vector, FRACTION_WIDTH)
print(vector)
u.printComplexFixedVector(fixed_vector, FRACTION_WIDTH+2, FRACTION_WIDTH)
