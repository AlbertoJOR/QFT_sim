def img_mul(a_real:float, a_img:float, b_real:float, b_img:float) -> (float, float):
    real_part = a_real * b_real 
    img_part =  a_img * b_img 
    res_real = real_part + -1*(img_part)
    res_img = a_real * b_img + a_img * b_real
    return (res_real, res_img)

def img_sum(a_real:float, a_img:float, b_real:float, b_img:float) -> (float, float):
    res_real = a_real + b_real
    res_img = a_img + b_img
    return (res_real, res_img)

def img_kara(a_real:float, a_img:float, b_real:float, b_img:float) -> (float, float):
    real_part = a_real * b_real 
    img_part =  a_img * b_img 
    res_real = real_part + -1*(img_part)
    res_img = (a_real + a_img)*(b_real + b_img) - real_part - img_part
    return (res_real, res_img)

def print_img(real, img):
    print("val : {:.4f} {:.4f} i".format(real, img))


res = img_mul(-3,5,-7,2)
print_img(res[0], res[1])
res = img_kara(-3,5,-7,2)
print_img(res[0], res[1])