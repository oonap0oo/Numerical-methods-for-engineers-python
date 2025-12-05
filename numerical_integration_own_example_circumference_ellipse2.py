# Calculating circumference ellipse using integration with Trapezoidal,
# Simpson's 1/3 and 3/8 rule coded in Python

from math import *

info = """Method to approximate the Circumference of an ellipse, using Python
-------------------------------------------------------------------

Ellipse:

        x²/a² + y²/b² = 1

Cicumference using Elliptic integral:

        e is the eccentricity of the ellipse:
        
        e = √( 1 - b² / a² ), a > b
        
                            π/2 
        Circumference = 4.a.∫ √( 1 - e².sin²(θ) ).d(θ)
                            0
"""

def integrand(theta):
    """Function to be integrated
    theta: independant variable"""
    return sqrt(1 - (eccentricity * sin(theta))**2)

# Trapezoidal rule
def trapm(a, b, n,f):
    """
    Trapezoidal rule for given function
    a: start of integration interval
    b: stop of integration interval
    n: number of segments
    f: function to integrate
    """
    delta_t = b - a
    h = delta_t / n
    sum = f(a)
    for i in range(1, n):
        sum += 2 * f(a + i * h)
    sum += f(b)
    return h * sum / 2, h


# Simpson's 1/3 rule
# Integral ≈ (b - a) * 1/6 * (f(x0) + 4*f(x1) + f(x2)) 
def simpsons13m(a ,b ,n ,f):
    """
    Simpson's 1/3 rule for given function
    a: start of integration interval
    b: stop of integration interval
    n: number of segments
    f: function to integrate
    """
    delta_t = b - a
    h = delta_t / n
    sum = f(a)
    for i in range(1, n-2, 2):
        sum += 4 * f(a + i * h) + 2 * f(a + (i+1) * h)
    sum += 4 * f(a + (n-1) * h) + f(a + n * h)
    return 2 * h * sum / 6, h

    
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
a_ellipse = 2 
b_ellipse = 1

# parameters Simpson's rule
n = 100 # number of iterations

print(f"Calculation for an example ellipse with a = {a_ellipse}  b = {b_ellipse}:")

eccentricity = sqrt(1 - b_ellipse**2 / a_ellipse**2)
print(f"\n        Eccentricity = {eccentricity}")

# Trapezoidal rule 
integral, h = trapm(0 ,pi/2 ,n ,integrand)
c0 = 4 * a_ellipse * integral
print(f"\n        Using Elliptic integral calculated with Trapezoidal rule coded in Python, {n} iterations:\n        Circumference = {c0}")

# Simpson's 1/3 rule
integral, h = simpsons13m(0 ,pi/2 ,n ,integrand)
c1 = 4 * a_ellipse * integral
print(f"\n        Using Elliptic integral calculated with Simpson's 1/3 rule coded in Python, {n} iterations:\n        Circumference = {c1}")

# Simpson's 3/8 rule
integral, h = simpsons38m(0 ,pi/2 ,n ,integrand)
c2 = 4 * a_ellipse * integral
print(f"\n        Using Elliptic integral calculated with Simpson's 3/8 rule coded in Python, {n} iterations:\n        Circumference = {c2}")

# Simple Arithmetic-Geometric Mean approximation
c3 = sqrt(2) * pi * sqrt(a_ellipse**2 + b_ellipse**2)
print(f"\n        Using Simple Arithmetic-Geometric Mean approximation:\n        Circumference = {c3}")

# Ramanujan's second approximation
h = (a_ellipse - b_ellipse)**2 / (a_ellipse + b_ellipse)**2
c4 = pi * (a_ellipse + b_ellipse) * (1 + 3 * h / (10 + sqrt(4 - 3 * h)))
print(f"\n        Using Ramanujan's second approximation:\n        Circumference = {c4}")


