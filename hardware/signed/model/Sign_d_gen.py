from util import *

float_val = 0.7071067811865475244008443
fixed_val = floatToSignedInt(float_val, 30)
print(float_val)
print(format(fixed_val, f'0{8}x').upper())
print()

float_val = -0.7071067811865475244008443
fixed_val = floatToSignedInt(float_val, 30)
print(float_val)
print(format(fixed_val, f'0{8}x').upper())
print()

float_val = -1
fixed_val = floatToSignedInt(float_val, 30)
print(float_val)
print(format(fixed_val, f'0{8}x').upper())
print()

float_val = 1
fixed_val = floatToSignedInt(float_val, 30)
print(float_val)
print(format(fixed_val, f'0{8}x').upper())
print()

float_val = -0.5
fixed_val = floatToSignedInt(float_val, 30)
print(float_val)
print(format(fixed_val, f'0{8}x').upper())
print()

float_val = 0.5
fixed_val = floatToSignedInt(float_val, 30)
print(float_val)
print(format(fixed_val, f'0{8}x').upper())
print()
