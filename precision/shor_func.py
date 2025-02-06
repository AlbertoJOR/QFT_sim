import cmath
import math

def bin_exp(base, exp, mod):
    res = 1
    base = base % mod

    while exp > 0:
        if (exp % 2) == 1:
            res = (res * base) % mod
        
        exp = exp >> 1  
        base = (base * base) % mod 

    return res
def complex_prob(z):
    z_con = z.conjugate()
    res = z * z_con
    return res.real

def func_c(c,r,q,l):
    amp = (math.sqrt(r)/q) * cmath.exp(2*math.pi*1j * (l*c/q))
    amp_aux = 0
    end = math.floor(q/r)
    for j in range(end):
        amp_aux = amp_aux + cmath.exp(2*math.pi*1j *(j * r * c /q))
    
    amp = amp * amp_aux

    return amp

def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a