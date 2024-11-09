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
def fixedPointStringComplex(value:str, D_W:int, point_index:int):
    res = []
    real_part = int(value.binstr[0:D_W])
    img_part = int(value.binstr[D_W:D_W*2])
    real_fixed = fixedPointString(real_part,D_W, point_index)
    img_fixed = fixedPointString(img_part,D_W, point_index)
    res.append(real_fixed)
    res.append(img_fixed)

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

def ComplexFloatToSignedInt(Real:float, Img:float, fraction:int, D_W: int):
    real_sint = floatToSignedInt(Real, fraction)
    img_sint = floatToSignedInt(Real, fraction)
    return (real_sint << D_W)|img_sint


def fixed_point_array (array_sig, N, D_W):
    data = []
    for i in range(N):
        data.append(fixedPointString(int(array_sig[i].value), D_W, D_W-2))
    return data 

def fixed_point_array_complex (array_sig, N, D_W):
    data = []
    for i in range(N):
        data.append(fixedPointStringComplex(array_sig[i].value, D_W, D_W-2))
    return data 


def print_fixed_double(array_r, array_i, name):
    N = len(array_r)
    print()
    for i in range(N):
        print(name + "[" + str(i) +"] R = " + array_r[i] +"   "+ "I = " + array_i[i] )

def print_fixed_complex(value_array, N, D_W, name):
    fixed_array = fixed_point_array_complex(value_array, N, D_W)
    print()
    for i in range(N):
        print(name + "[" + str(i) +"] R = " + fixed_array[i][0] +"   "+ "I = " + fixed_array[i][1] )

    
    


