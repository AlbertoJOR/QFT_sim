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





