def generate_sequence(n):
    if n == 1:
        return [2]
    else:
        previous_sequence = generate_sequence(n - 1)
        return [n + 1] + previous_sequence + previous_sequence

# Ejemplo de uso:
n = 5
result = generate_sequence(n)
print(result)

