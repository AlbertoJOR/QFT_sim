def mask_int (a: int, data_w:int) -> int:

    mask = (1 << data_w) - 1 
    masked = a & mask

    return masked


def complex_mul(a_real:int, a_img:int, b_real:int, b_img:int, data_W:int) -> (int, int):

    real_part = a_real * b_real 
    img_part =  a_img * b_img 
    res_real = real_part + -1*(img_part)
    res_img = a_real * b_img + a_img * b_real

    return (mask_int(res_real, data_W*2), mask_int(res_img, data_W*2))

def complex_sum(a_real:int, a_img:int, b_real:int, b_img:int) -> (int, int):

    res_real = a_real + b_real
    res_img = a_img + b_img

    return (res_real, res_img)