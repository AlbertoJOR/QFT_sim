def inverter_module(a: int) -> int :
    """model of module inverter"""
    return (~a) + 1

def multiplication(a: int , b: int) -> int:
    return a * b
a = 5
b = 7
neg_a = inverter_module(a)
negneg_a = inverter_module(neg_a)

mult1 = multiplication(a, b)
mult2 = multiplication(a, inverter_module(b))
mult3 = multiplication(b, inverter_module(a))
mult4 = multiplication(inverter_module(b), inverter_module(a))

print('{:08x}'.format(a))
print('{:08x}'.format(neg_a))
print('{:08x}'.format(neg_a))

print()

print('{:08x}'.format(mult1))
print('{:08x}'.format(mult2))
print('{:08x}'.format(mult3))
print('{:08x}'.format(mult4))