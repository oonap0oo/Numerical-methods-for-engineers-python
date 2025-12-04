from math import *

info = """Method to approximate the Circumference of an ellipse, using Python
-------------------------------------------------------------------

Ellipse:
--------

        x²/a² + y²/b² = 1

Method 1, Elliptic integral:
----------------------------

        e is the eccentricity of the ellipse:
        
        e = √( 1 - b² / a² ), a > b
        
                            π/2 
        Circumference = 4.a.∫ √( 1 - e².sin²(θ) ).d(θ)
                            0

Method 2, Simple Arithmetic-Geometric Mean approximation:
---------------------------------------------------------

        Circumference ≈ √(2).π.√( a² + b² )    
"""

def integrand(theta):
    """Function to be integrated
    theta: independant variable"""
    return sqrt(1 - (eccentricity * sin(theta))**2)

    
# Simpson's 3/8 rule
# Integral ≈ (b - a) * 1/8 * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3)) 
def simpsons38m(a ,b ,n ,f):
    """
    Simpson's 3/8 rule for given function
    a: start of integration interval
    b: stop of integration interval
    n: number of segments
    f: function to integrate
    """
    n_mod = (n // 3 + 1) * 3 # modify n so it is multiple of 3
    delta_t = b - a
    h = delta_t / n_mod
    sum = f(a) # the first part to the addition
    for i in range(1, n_mod-3, 3):
        sum += 3 * f(a + i * h) + 3 * f(a + (i+1) * h) + 2 * f(a + (i+2) * h)
    sum += 3 * f(a + (n_mod-2) * h) + 3 * f(a + (n_mod-1) * h) + f(a + n_mod * h) # the last 3 parts are added
    return 3 * h * sum / 8, h


print(info)

# parameters Ellipse
a = 2 
b = 1

# parameters Simpson's rule
n = 100 # nume-ber of iterations

print(f"\nCalculation for an example ellipse with a = {a}  b = {b}:")
print("------------------------------------------------------")

eccentricity = sqrt(1 - b**2 / a**2)
print(f"\n        Eccentricity = {eccentricity}")

integral, h = simpsons38m(0 ,pi/2 ,n ,integrand)
c1 = 4 * a * integral
print(f"\n        Using Elliptic integral calculated with Simpson's 3/8 rule coded in Python:\n        Circumference = {c1}")

c2 = sqrt(2) * pi * sqrt(a**2 + b**2)
print(f"\n        Using Simple Arithmetic-Geometric Mean approximation:\n        Circumference = {c2}")


