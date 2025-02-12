import util as u
import math
import numpy as np
import random

def complexMultFixed(a_real :int, a_img: int, b_real : int, b_img : int, D_W: int, F_W: int):
    pass

def signedIntToFloat(fixed_point: int, F_W: int) -> float:
    sign_bit_position = F_W + 1  
    sign_mask = 1 << sign_bit_position 

    sign = (fixed_point & sign_mask) != 0 
    value_mask = (1 << sign_bit_position) - 1 

    abs_value = fixed_point & value_mask  
    float_value = abs_value / (2 ** F_W) 

    return -float_value if sign else float_value 

def flipSignedIntSign(A: int , D_W: int) -> int:
    sign_mask = 1 << (D_W-1) 
    return sign_mask ^ A



def multiplySignedFixedPoint(A: int, B: int, F_W: int, D_W: int) -> int:
    # 1. Extraer el bit de signo (MSB)
    sign_mask = 1 << (D_W - 1)  # Ejemplo: si D_W=8 -> 0b10000000
    sign_A = (A & sign_mask) != 0
    sign_B = (B & sign_mask) != 0

    # 2. Extraer los valores absolutos sin el bit de signo
    value_mask = sign_mask - 1  # Máscara para obtener la parte entera y fracción
    abs_A = A & value_mask
    abs_B = B & value_mask

    # 3. Multiplicar las partes sin signo
    product = abs_A * abs_B  # Ahora es Q(2*F_W)

    # 4. Ajustar la escala dividiendo por 2^F_W (desplazamiento)
    result = (product >> F_W)  # Equivalente a dividir por 2^F_W

    # 5. Restaurar el signo con OR si es necesario
    if sign_A ^ sign_B:  # XOR: Si los signos son distintos, el resultado debe ser negativo
        result |= sign_mask  # Aplicamos el bit de signo al resultado

    return result


def addSubtractSignedFixedPoint(A: int, B: int, F_W: int, D_W: int) -> int:
    # Máscara para el bit de signo (MSB)
    sign_mask = 1 << (D_W - 1)
    
    # Extraemos el signo de A y B
    sign_A = (A & sign_mask) != 0
    sign_B = (B & sign_mask) != 0
    
    # Máscara para las partes absolutas (sin el bit de signo)
    value_mask = sign_mask - 1
    abs_A = A & value_mask
    abs_B = B & value_mask

    # Si los signos son iguales, sumamos los valores absolutos
    if sign_A == sign_B:
        result = abs_A + abs_B  # Sumar
    else:
        # Si los signos son diferentes, restamos los valores absolutos
        if abs_A >= abs_B:
            result = abs_A - abs_B  # Restar
        else:
            result = abs_B - abs_A  # Restar (el resultado será positivo si B es mayor)

# 
    # Restaurar el signo según el resultado
    if sign_A == sign_B:  # Si los signos son iguales, el resultado conserva el signo
        if sign_A:  # Si ambos son negativos
            result |= sign_mask  # Aplicamos el bit de signo
    else:
        if abs_A >= abs_B:
            if sign_A:  # Si A es negativo, el resultado también será negativo
                result |= sign_mask
        else:
            if sign_B:  # Si B es negativo, el resultado será negativo
                result |= sign_mask

    return result

def divideSignedFixedPoint(A: int, B: int, F_W: int, D_W: int) -> int:
    # 1. Extraer el bit de signo (MSB)
    sign_mask = 1 << (D_W - 1)  # Máscara de signo (MSB)
    sign_A = (A & sign_mask) != 0
    sign_B = (B & sign_mask) != 0

    # 2. Extraer los valores absolutos sin el bit de signo
    value_mask = sign_mask - 1  # Máscara para obtener la parte entera y fracción
    abs_A = A & value_mask
    abs_B = B & value_mask

    # 3. Dividir las partes absolutas
    if abs_B == 0:
        raise ValueError("División por cero no permitida")  # Comprobar división por cero
    quotient = abs_A * (1 << F_W) // abs_B  # Realizamos el desplazamiento para mantener la precisión

    # 4. Ajuste de escala: el resultado ya tiene la escala correcta por el desplazamiento
    # El resultado está en Q(F_W), por lo que no necesitamos hacer más ajustes de escala

    # 5. Restaurar el signo con XOR si es necesario
    if sign_A != sign_B:  # Si los signos son diferentes, el resultado será negativo
        quotient |= sign_mask  # Aplicamos el bit de signo al resultado

    return quotient

def multiplyComplexFixedPoint(A_real: int, A_img: int, B_real: int, B_img:int, F_W :int, D_W:int) -> (int, int):
    arbr = multiplySignedFixedPoint(A_real, B_real, F_W, D_W)
    arbi = multiplySignedFixedPoint(A_real, B_img, F_W, D_W)
    aibr = multiplySignedFixedPoint(A_img, B_real, F_W, D_W)
    aibi = multiplySignedFixedPoint(A_img, B_img, F_W, D_W)
    aibi_neg = flipSignedIntSign(aibi, D_W)
    # u.printFixedPoint(arbr, D_W, F_W)
    # u.printFixedPoint(arbi, D_W, F_W)
    # u.printFixedPoint(aibr, D_W, F_W)
    # u.printFixedPoint(aibi, D_W, F_W)
    # u.printFixedPoint(aibi_neg, D_W, F_W)
    res_r = addSubtractSignedFixedPoint(arbr, aibi_neg, F_W , D_W)
    res_i = addSubtractSignedFixedPoint(aibr, arbi, F_W, D_W)
    return(res_r, res_i)

def addComplexFixedPoint(A_real: int, A_img: int, B_real: int, B_img:int, F_W :int, D_W:int) -> (int, int):
    res_r = addSubtractSignedFixedPoint(A_real, B_real, F_W , D_W)
    res_i = addSubtractSignedFixedPoint(A_img, B_img, F_W, D_W)
    return(res_r, res_i)

def absValueComplexFixedPoint(A_real: int, A_img: int,  F_W :int, D_W:int) -> int:
    A_img_complement = flipSignedIntSign(A_img, D_W)
    res_r, res_i = multiplyComplexFixedPoint(A_real, A_img, A_real, A_img_complement, F_W, D_W)
    return res_r

def tensorProductComplexFixed(A, B, F_W, D_W):
    
    
    rows_A, cols_A = len(A), len(A[0])  
    rows_B, cols_B = len(B), len(B[0])  


    result = [[(0, 0) for _ in range(cols_A*cols_B)] for _ in range(rows_A * rows_B)]


    for i in range(rows_A):
        for j in range(cols_A):
            for k in range(rows_B):
                for l in range(cols_B):
                    a_real = A[i][j][0]
                    a_img = A[i][j][1]
                    b_real = B[k][l][0]
                    b_img = B[k][l][1]
                    result[i * rows_B + k][j * cols_B + l] =  multiplyComplexFixedPoint(a_real, a_img, b_real, b_img, F_W, D_W)

    return result


def randomComplexFloat():
    real = random.uniform(-1, 1)
    imag = random.uniform(-1, 1)
    return (real, imag)

def complexNorm(vector):
    return math.sqrt(sum(r**2 + i**2 for r, i in vector))

def normalizeComplexVector(size):
    vector = [randomComplexFloat() for _ in range(size)]
    norm = complexNorm(vector)
    return [(r / norm, i / norm) for r, i in vector]

def randomNormComplexFixedPVector(size, F_W):
    floatVector = normalizeComplexVector(size)
    fixedVector = [(0, 0) for _ in range(size)]
    for i in range(size):
        fixedVector[i] = u.complexToFixedTuple(floatVector[i], F_W)
    return fixedVector

def complexVectorToFixed(floatVector, F_W):
    size = len(floatVector)
    fixedVector = [(0, 0) for _ in range(size)]
    for i in range(size):
        fixedVector[i] = u.complexToFixedTuple(floatVector[i], F_W)
    return fixedVector

def randComplexMatrix(rows, cols, F_W):
    result = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            a_real = random.random();
            a_img = random.random();
            ar_fix = u.floatToSignedInt(a_real, F_W)
            ai_fix = u.floatToSignedInt(a_img, F_W)
            result[i][j] = (ar_fix, ai_fix)
    return result

def complexMatrixToFixed(floatM, F_W):
    rows, cols = len(floatM), len(floatM[0])  
    result = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = u.complexToFixedTuple(floatM[i][j], F_W)
    return result

def ComplexFixDotProduct(vecA, vecB, F_W, D_W):
    size = len(vecA)
    result = [(0,0) for _ in range(size)]
    for i in range(size):
        a_real = vecA[i][0]
        a_img = vecA[i][1]
        b_real = vecB[i][0]
        b_img = vecB[i][1]
        result[i] =  multiplyComplexFixedPoint(a_real, a_img, b_real, b_img, F_W, D_W)
    accum = (0,0)
    for i in range(size):
        accum = addComplexFixedPoint(accum[0], accum[1], result[i][0], result[i][1], F_W, D_W)
    return accum



def ComplexFixedVectorMatrixMult(vector, matrix, F_W, D_W):
    size = len(vector)
    result = [(0,0) for _ in range(size)]
    for i in range(size):
        result[i] =  ComplexFixDotProduct(vector, matrix[i], F_W, D_W)
    return result



#####       Shor function
def modularExponentiationVector(a, N, n):
    size = 2 ** (2 * n)
    q = 2 ** n
    
    vector = np.zeros(size, dtype=complex)
    
    amplitude = 1 / np.sqrt(q)
    
    for i in range(q):
        a_i_mod_N = pow(a, i, N)
        # Encontrar el índice en el espacio de estado |i>|a^i mod N> 
        index =  i * (2 ** n) + a_i_mod_N
        if(index < size) :
            vector[index] = amplitude
    
    return vector

def modularExponentiationVectorCFP(a, N, n, F_W):
    size = 2 ** (2 * n)
    q = 2 ** n
    
    vector = [(0, 0) for _ in range(size)]
    
    amplitude = 1 / np.sqrt(q)
    amplitudefp = u.floatToSignedInt(amplitude, F_W)
    
    for i in range(q):
        a_i_mod_N = pow(a, i, N)
        # Encontrar el índice en el espacio de estado |i>|a^i mod N> 
        index =  i * (2 ** n) + a_i_mod_N
        if(index < size) :
            vector[index] = (amplitudefp, 0) 
    
    return vector

def qfti(vector, n):

    N = 2 ** n
    
    # Crear la matriz de la QFTI
    qfti_matrix = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            qfti_matrix[j, k] = (1 / np.sqrt(N)) * np.exp(2j * np.pi * j * k / N)
    
    # Aplicar la QFTI al vector
    result = np.dot(qfti_matrix, vector)
    
    return result

def IdentityMatrixCPF(rows, F_W):
    result = [[(0, 0) for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        ar_fix = u.floatToSignedInt(1.0, F_W)
        ai_fix = u.floatToSignedInt(0.0, F_W)
        result[i][i] = (ar_fix, ai_fix)
    return result

def qftiCFP(vector, n, F_W, D_W):

    N = 2 ** n
    
    # Crear la matriz de la QFTI
    qfti_matrix = [[(0, 0) for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for k in range(N):
            complexval = (1 / np.sqrt(N)) * np.exp(2j * np.pi * j * k / N)
            real = complexval.real
            img = complexval.imag
            qfti_matrix[j][k] = u.complexToFixedTuple((real, img), F_W)
    
    # u.printComplexFixedMatrix(qfti_matrix, D_W, F_W)
    
    # Aplicar la QFTI al vector
    result = ComplexFixedVectorMatrixMult(vector, qfti_matrix, F_W, D_W)
    
    return result

def qftTensorCFP(vector, n , F_W, D_W):
    N = 2 ** n
    
    # Crear la matriz de la QFTI
    qfti_matrix = [[(0, 0) for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for k in range(N):
            complexval = (1 / np.sqrt(N)) * np.exp(2j * np.pi * j * k / N)
            real = complexval.real
            img = complexval.imag
            qfti_matrix[j][k] = u.complexToFixedTuple((real, img), F_W)
    
    # u.printComplexFixedMatrix(qfti_matrix, D_W, F_W)
    
    identity_matrix = IdentityMatrixCPF(N, F_W)
    tensor = tensorProductComplexFixed(qfti_matrix, identity_matrix, F_W, D_W)
    result = ComplexFixedVectorMatrixMult(vector, tensor, F_W, D_W)
    
    return result
