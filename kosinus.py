import math
from sinus import abs

def cos_taylor(x, n):
    """
    Berechnet cos(x) mit der Taylorreihe bis zum n-ten Summanden.
    
    x : float  (Radiant!)
    n : int    (Anzahl der Summanden)
    """
    result = 0.0
    for k in range(n + 1):
        term = (-1)**k * x**(2*k) / math.factorial(2*k)
        result += term
    return result


# Beispiel
x = math.pi / 3
n = 75

cos_t=cos_taylor(x, n)
cos_m=math.cos(x)
print()
print()
print()
print("Taylor-Approximation:", cos_t)
print("math.cos(x):         ", cos_m)
print("Abweichung:          ", abs(cos_t-cos_m))
print()
print()