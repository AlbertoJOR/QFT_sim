def mask_int (a: int, data_w:int) -> int:
    mask = (1 << data_w) - 1 
    masked = a & mask
    return masked

def mask_bit (a: int, index: int) -> int :
    mask = 1 << (index - 1)
    return mask & a

def signedString(A:int, D_W:int):
    sign_bit = mask_bit(A, D_W)
    magnitud = mask_int (A, D_W-1)
    sign = "-" if sign_bit else " "
    return "{}{}".format(sign,magnitud)





