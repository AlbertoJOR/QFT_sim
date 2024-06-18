import math
def mask_int (a: int, data_w:int) -> int:
    mask = (1 << data_w) - 1 
    masked = a & mask
    return masked

def mask_part_int (a: int, data_w:int, fixed:int) -> int:
    mask = (1 << data_w) - 1 
    masked = (a & mask) >> fixed
    return masked

def mask_bit (a: int, index: int) -> int :
    mask = 1 << (index - 1)
    return mask & a

def shiftLeftBit (sign:bool, data_w :int) ->int:
    if(sign):
        return 1<<(data_w-1)
    else:
        return 0

def signedString(A:int, D_W:int):
    sign_bit = mask_bit(A, D_W)
    magnitud = mask_int (A, D_W-1)
    sign = "-" if sign_bit else " "
    return "{}{}".format(sign,magnitud)

def fixedPointString(A:int, D_W:int, point_index: int):
    sign_bit = mask_bit(A, D_W)
    magnitud = mask_int(A, D_W-1)
    sign = "-" if sign_bit else " "



    fixed_point_value = magnitud / (2 ** point_index)
    decimal_digits = math.ceil(point_index * math.log10(2)) +1 

    # fixed_point_str = sign + f"{fixed_point_value:.{point_index}f}"
    fixed_point_str = sign + f"{fixed_point_value:.{decimal_digits}f}"
    
    return fixed_point_str

def intToSignedInt(A:int, D_W:int, sign:bool)->int:
    sign = shiftLeftBit(sign,D_W)
    return A | sign

def floatToSignedInt(A:float, fraction:int) -> int:
    scale = 2 ** fraction
    sign = False
    float_val = A
    if A <0:
        sign = True
        float_val = -1*A
        
    sign_val = shiftLeftBit(sign, fraction+2)

    fixed_point = int(round(float_val*scale))
    if sign:
        fixed_point = sign_val | fixed_point
    return fixed_point

    

# float_val = -0.7071067811865475244008443
# fixed_val = floatToSignedInt(float_val, 14)
# print(float_val)
# print(format(fixed_val, f'0{16}b'))
# print()

# float_val = 0.7071067811865475244008443
# fixed_val = floatToSignedInt(float_val, 14)
# print(float_val)
# print(format(fixed_val, f'0{16}b'))

# float_val = -1
# fixed_val = floatToSignedInt(float_val, 14)
# print(float_val)
# print(format(fixed_val, f'0{16}b'))
# print()

# float_val = 1 
# fixed_val = floatToSignedInt(float_val, 14)
# print(float_val)
# print(format(fixed_val, f'0{16}b'))

