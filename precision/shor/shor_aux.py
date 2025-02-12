import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

def initialize_superposition_vector(n):
    """
    Inicializa un vector cuántico  como |i, 0> de i = 0 hasta 2^(n)-1
    
    Args:
        n (int): El número de qubits, determinando el tamaño del vector (2^n).
        
    Returns:
        np.ndarray, complex: Un vector con amplitudes uniformes distribuidas en todos los estados posibles. 
        del doble de tamaño en qubits
    """
    size = 2 ** (2 * n)
    N = 2 ** n
    
    vector = np.zeros(size, dtype=complex)
    
    amplitude = 1 / np.sqrt(N)
    for i in range(N):
        vector[N*i] = amplitude
    
    return vector


def modula_exponentiation_vector(a, N, n):
    """
    Se aplica la función f(a) o exponenciación modular en la forma |i, a^i mod N> 
    donde a^i mod N está en los primeros n qubits, y |i> está en los siguientes n qubits. 
    Todos los estados tienen la misma amplitud.
    
    Args:
        a (int): La base para la exponenciación modular.
        N (int): Modulo N.
        n (int): El número de qubits, determinando el tamaño del vector (2^n).
        
    Returns:
        np.ndarray: Un vector con amplitudes uniformes distribuidas en todos los estados posibles.
    """
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

def qfti(vector, n):
    """
    Aplica la Transformada Cuántica de Fourier Inversa (QFTI) a un vector dado.
    
    Args:
        vector (np.ndarray): Un vector de entrada en el espacio de Hilbert de tamaño 2^n.
        n (int): El número de qubits (número de qubits que define el tamaño del vector de entrada).
        
    Returns:
        np.ndarray: El vector resultante después de aplicar la QFTI.
    """
    N = 2 ** n
    
    # Crear la matriz de la QFTI
    qfti_matrix = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            qfti_matrix[j, k] = (1 / np.sqrt(N)) * np.exp(2j * np.pi * j * k / N)
    
    # Aplicar la QFTI al vector
    result = np.dot(qfti_matrix, vector)
    
    return result

def qfti_values(vector, n):
    """
    Aplica la Transformada Cuántica de Fourier Inversa (QFTI) a un vector dado.
    
    Args:
        vector (np.ndarray): Un vector de entrada en el espacio de Hilbert de tamaño 2^n.
        n (int): El número de qubits (número de qubits que define el tamaño del vector de entrada).
        
    Returns:
        np.ndarray: El vector resultante después de aplicar la QFTI.
    """
    N = 2 ** n
    
    # Crear la matriz de la QFTI
    qfti_matrix = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            qfti_matrix[j, k] =  np.exp(2j * np.pi * j * k / N)
    
    # Aplicar la QFTI al vector
    # result = np.dot(qfti_matrix, vector)
    result = qfti_matrix
    
    return result

def qfti_index(vector, n):
    """
    Aplica la Transformada Cuántica de Fourier Inversa (QFTI) a un vector dado utilizando una lista de valores precomputados.
    
    Args:
        vector (np.ndarray): Un vector de entrada en el espacio de Hilbert de tamaño 2^n.
        n (int): El número de qubits (número de qubits que define el tamaño del vector de entrada).
        
    Returns:
        np.ndarray: El vector resultante después de aplicar la QFTI.
    """
    N = 2 ** n
    
    # Precomputar los posibles valores de la matriz QFTI
    qfti_values = [np.exp(2j * np.pi * i / N) for i in range(N)]
    
    # Crear la matriz de la QFTI utilizando los valores precomputados
    qfti_matrix = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            qfti_matrix[j, k] = qfti_values[(j * k) % N]
    
    # Aplicar la QFTI al vector
    # result = np.dot(qfti_matrix, vector)
    result = qfti_matrix
    
    return result

def qfti_tensor_product(vector, n):
    """
    Aplica el producto tensorial de la Transformada Cuántica de Fourier Inversa (QFTI) con la identidad
    a un vector de estado cuántico de 2^2n dimensiones, a los qubits más significativos.
    
    Args:
        vector (np.ndarray): Un vector de entrada en el espacio de Hilbert de tamaño 2^(2n).
        n (int): El número de qubits significativos a los que se les aplica la QFTI.
        
    Returns:
        np.ndarray: El vector resultante después de aplicar QFTI ⊗ I.
    """
    
    
    N_qfti = 2 ** n
    
    # Crear la matriz de la QFTI para los primeros n qubits
    qfti_matrix = np.zeros((N_qfti, N_qfti), dtype=complex)
    for j in range(N_qfti):
        for k in range(N_qfti):
            qfti_matrix[j, k] = (1 / np.sqrt(N_qfti)) * np.exp(-2j * np.pi * j * k / N_qfti)
    
    # Crear la matriz identidad para los últimos n qubits
    identity_matrix = np.eye(N_qfti, dtype=complex)
    
    # Calcular el producto tensorial QFTI ⊗ I
    qfti_tensor = np.kron(qfti_matrix, identity_matrix)
    
    result = np.dot(qfti_tensor, vector)
    
    return result


def complex_prob(z):
    z_con = z.conjugate()
    res = z * z_con
    return res.real


def complexvec_prob(vector):
    vector_prob = np.zeros(vector.size, dtype=float)
    for i in range(0,vector.size):
        vector_prob[i] = complex_prob(vector[i])
    return vector_prob

def sum_prob(vector):
    sum = 0
    for val in vector:
        sum = sum + val
    return sum 

def projection_msb(estado, total_qubits, n):
    num_states = 2**n
    proj = np.zeros(num_states, dtype=float)
    
    for i in range(num_states):
        index = [i * num_states + j for j in range(2**(n))]
        prob_vector = complex_prob(estado[index])
        proj[i] = sum_prob(prob_vector)
        
    return proj


        

def save_csv(vector, file_name, n):
    and_mask = 2 ** (2*n) - 1
    msb_mask = and_mask << n
    lsb_mask = and_mask >> n 
    bin_length = '0' + str(n) + 'b'        
    vector_size = vector.size
    comma = ', '
    heading = '|i  mod>, |i  mod>, prob, amp'
    with open(file_name + '.csv', 'w') as f:
        f.write(heading + '\n')
        for i in range(0, vector_size):
            msb = (i & msb_mask) >>n
            lsb = i & lsb_mask
            msb_bin_string = format(msb, bin_length)
            lsb_bin_string = format(lsb, bin_length) 
            msb_string = str(msb)
            lsb_string = str(lsb)
            prob = str(complex_prob(vector[i]))
            amplitud = str(vector[i])
            string_save = '|' +msb_bin_string+' ' + lsb_bin_string +'>' + comma + '|'+ msb_string + ' ' + lsb_string+ '>' + comma + prob + comma + amplitud
            f.write(string_save + '\n')

def save_csv2(vector, file_name, n):
    bin_length = '0' + str(n) + 'b'        
    vector_size = vector.size
    comma = ', '
    heading = '|i >, |i >, prob, amp'
    with open(file_name + '.csv', 'w') as f:
        f.write(heading + '\n')
        for i in range(0, vector_size):
            bin_string = format(i, bin_length)
            qbit_string = str(i)
            prob = str(complex_prob(vector[i]))
            amplitud = str(vector[i])
            string_save = '|' +bin_string +'>' + comma + '|'+ qbit_string + '>' + comma + prob + comma + amplitud
            f.write(string_save + '\n')

def return_label_double(len, n):
    and_mask = 2 ** (2*n) - 1
    msb_mask = and_mask << n
    lsb_mask = and_mask >> n 
    labels = []
    for i in range(len):
        msb = (i & msb_mask) >>n
        lsb = i & lsb_mask
        msb_string = str(msb)
        lsb_string = str(lsb)
        labels.append('|' +msb_string+' ' + lsb_string +'>')
    return labels
    
def return_label(len, n):
    and_mask = 2 ** (n) - 1
    labels = []
    for i in range(len):
        msb_string = str(i)
        labels.append('|' +msb_string + '>')
    return labels
    


 
def prob_barplot(vector, n, figname):

    prob_val = complexvec_prob(vector)

    bin_len = '0' + str(n) + 'b'
    etiquetas = ['|'+format(i,bin_len)+'>' for i in range(len(vector))]

    ancho_barras = 0.4
    val_pos = np.arange(len(vector))

    fig, ax = plt.subplots()

    ax.bar(val_pos, prob_val, width=ancho_barras, color='b', alpha=0.6, label='R')


    ax.set_xlabel('qubits')
    ax.set_ylabel('amplitud')
    ax.set_xticks(val_pos + ancho_barras / 16)
    ax.set_xticklabels(etiquetas)
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right") 

    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=8))

    plt.tight_layout()
    # ax.legend()


    plt.savefig(figname)



def prob_barplot2(vector, n, figname, complex_val = True):
    if(complex_val):
        prob_val = complexvec_prob(vector)  
    else :
        prob_val = vector

    bin_len = '0' + str(n) + 'b'
    etiquetas = ['|'+format(i,bin_len)+'>' for i in range(len(vector))]

    ancho_barras = 0.4
    val_pos = np.arange(len(vector))

    fig, ax = plt.subplots()

    ax.bar(val_pos, prob_val, width=ancho_barras, color='b', alpha=0.6, label='R')

    ax.set_xlabel('qubits')
    ax.set_ylabel('amplitud')

    ax.set_xticks(val_pos)  
    ax.set_xticklabels(etiquetas)

    plt.setp(ax.get_xticklabels(), rotation=90, ha="right")

    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=8))

    plt.tight_layout()

    plt.savefig(figname)


def shor(N, a):
    n = math.ceil(math.log2(N)) 
    n2 = 2*n
    init_vector = initialize_superposition_vector(n)
    save_csv(init_vector,"ex/table1",n)
    init_vector_prob = complexvec_prob(init_vector)
    init_labels = return_label_double(init_vector.size,n)

    # funcion modular
    mod_vector = modula_exponentiation_vector(a, N ,n)
    save_csv(mod_vector,"ex/table2",n)
    mod_vector_prob = complexvec_prob(mod_vector)
    mod_labels = return_label_double(mod_vector.size,n)

    qfti_vector = qfti_tensor_product(mod_vector,n)
    save_csv(qfti_vector,"ex/table3",n)
    qfti_vector_prob = complexvec_prob(qfti_vector)
    qfti_labels = return_label_double(qfti_vector.size,n)

    proj_vector = projection_msb(qfti_vector,n2, n)
    proj_labels = return_label(proj_vector.size,n)
    values = [
        [init_vector_prob, mod_vector_prob, qfti_vector_prob, proj_vector],
        [init_labels, mod_labels, qfti_labels, proj_labels]
    ]
    return values