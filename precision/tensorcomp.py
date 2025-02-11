def complex_mult(c1, c2):
    """Multiplica dos números complejos representados como tuplas (real, imag)"""
    real1, imag1 = c1
    real2, imag2 = c2
    return (real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2)

def tensor_product(A, B):
    """ Calcula el producto tensorial de dos matrices con números complejos """
    
    rows_A, cols_A = len(A), len(A[0])  # Dimensiones de A
    rows_B, cols_B = len(B), len(B[0])  # Dimensiones de B

    # Matriz resultado con tamaño (rows_A * rows_B) x (cols_A * cols_B)
    result = [[(0, 0) for _ in range(cols_A * cols_B)] for _ in range(rows_A * rows_B)]

    # Multiplicación tensorial
    for i in range(rows_A):
        for j in range(cols_A):
            for k in range(rows_B):
                for l in range(cols_B):
                    result[i * rows_B + k][j * cols_B + l] = complex_mult(A[i][j], B[k][l])

    return result

def print_complex_matrix(matrix):
    """Imprime una matriz de números complejos de forma legible"""
    for row in matrix:
        print(" ".join(f"({r:.5f} {i:+.5f}i)" for r, i in row))
    print()

# Matriz A (2x2) con números complejos
A = [
    [(0.84668, 0.05249), (0.85889, 0.70679)],
    [(0.22412, 0.03760), (0.11768, 0.83447)]
]

# Matriz B (2x2) con números complejos
B = [
    [(0.97021, 0.15967), (0.04858, 0.41602)],
    [(0.36206, 0.75269), (0.19360, 0.40674)]
]

print("Matriz A:")
print_complex_matrix(A)

print("Matriz B:")
print_complex_matrix(B)

# Producto tensorial
tensor_result = tensor_product(A, B)

print("Producto Tensorial A ⊗ B:")
print_complex_matrix(tensor_result)


