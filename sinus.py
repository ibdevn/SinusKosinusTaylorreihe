import math

def sin_taylor(x, n):
    """
    Berechnet sin(x) mit der Taylorreihe bis zum n-ten Summanden.
    
    x : float  (Wert in Radiant!)
    n : int    (Anzahl der Summanden)
    """
    result = 0.0
    for k in range(n + 1):
        term = (-1)**k * x**(2*k + 1) / math.factorial(2*k + 1)
        result += term
    return result

def abs(x: float) -> float:
    return x if x>0 else -x
# Beispiel
x = math.pi / 2  
n = 75

sin_tay=sin_taylor(x, n)
sin_math=math.sin(x)

print()
print()
print("Taylor-Approximation:", sin_tay)
print("math.sin(x):         ", sin_math)
print("Abweichung:          ", abs(sin_math-sin_tay))

print()
print()
print()