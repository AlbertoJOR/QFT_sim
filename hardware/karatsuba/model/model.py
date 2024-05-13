def inverter_module(a: int) -> int :
    """model of module inverter"""
    return (~a) + 1

def multiplication(a: int , b: int) -> int:
    return a * b

def sign_extend(value, input_bits, output_bits):
    # Calculate the maximum positive value for the input bit length
    max_positive_value = 2 ** (input_bits - 1) - 1
    
    # Check if the most significant bit (MSB) is 1
    if value & (1 << (input_bits - 1)):
        # If it's 1, then sign extend by filling the upper bits with 1s
        extension = (2 ** output_bits) - (2 ** input_bits)
        return value | extension
    else:
        # If it's 0, then sign extend by filling the upper bits with 0s
        return value
# a = 5
# b = 7
# neg_a = inverter_module(a)
# negneg_a = inverter_module(neg_a)

# mult1 = multiplication(a, b)
# mult2 = multiplication(a, inverter_module(b))
# mult3 = multiplication(b, inverter_module(a))
# mult4 = multiplication(inverter_module(b), inverter_module(a))

# print('{:08x}'.format(a))
# print('{:08x}'.format(neg_a))
# print('{:08x}'.format(neg_a))

# print()

# print('{:08x}'.format(mult1))
# print('{:08x}'.format(mult2))
# print('{:08x}'.format(mult3))
# print('{:08x}'.format(mult4))
