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

def karatsuba_binary(A, B):
    # Convert A and B to binary strings
    A_bin = bin(A)[2:]
    B_bin = bin(B)[2:]
    
    # Pad with leading zeros to make the length 32 bits
    A_bin = '0' * (32 - len(A_bin)) + A_bin
    B_bin = '0' * (32 - len(B_bin)) + B_bin
    
    # Split A and B into high and low halves
    A_high = int(A_bin[:16], 2)
    A_low = int(A_bin[16:], 2)
    B_high = int(B_bin[:16], 2)
    B_low = int(B_bin[16:], 2)
    
    # Compute intermediate products
    P1 = A_high * B_high
    P2 = A_low * B_low
    P3 = (A_high + A_low) * (B_high + B_low)
    
    # Compute the final result
    Result = (P1 << 32) + ((P3 - P1 - P2) << 16) + P2
    
    return Result

