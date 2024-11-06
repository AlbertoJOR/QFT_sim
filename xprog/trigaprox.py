import math

def sin_approx(x):
    # Reducción de rango
    x = x % (2 * math.pi)  
    # Aproximación de Taylor
    result = x - (x**3) / 6 + (x**5) / 120 - (x**7) / 5040
    return result

def cos_approx(x):
    # Reducción de rango
    x = x % (2 * math.pi)  
    # Aproximación de Taylor
    result = 1 - (x**2) / 2 + (x**4) / 24 - (x**6) / 720
    return result

# Ejemplo de uso
x = 0.5  # Ángulo en radianes

print(f"sin({x}) ≈ {sin_approx(x)},  {math.sin(x)}")
print(f"cos({x}) ≈ {cos_approx(x)}, {math.cos(x)}")

sudo apt-get install git help2man perl python3 make autoconf g++ flex bison ccache
sudo apt-get install libgoogle-perftools-dev numactl perl-doc
sudo apt-get install libfl2  # Ubuntu only (ignore if gives error)
sudo apt-get install libfl-dev  # Ubuntu only (ignore if gives error)
sudo apt-get install zlibc zlib1g zlib1g-dev  # Ubuntu only (ignore if gives error)

