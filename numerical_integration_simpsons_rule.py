# Numerical Integration based on the book NUMERICAL METHODS FOR ENGINEERS 8th Edition
# Trapezoidal rule and Simpsons rule adapted from pseudocode on page 632
# applied on Example 21.3 on page 622 and 623

from math import *

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
    return 3 * h * sum / 8, h, n_mod


# The velocity of a falling object with air resistance
# where g is acceleration due to gravity
# m is mass
# c is the drag coefficient
# t is time
def velocity(t):
    """velocity as funtion of time"""
    return g * m / c * (1 - exp(-(c * t / m)) )


g = 9.8 # m/s² acceleration due to gravity
m = 68.1 # kg mass
c = 12.5 # kg/s drag coefficient

distance_exact = 289.43515 # m

segments = [a*b for b in [1,10,100] for a in [1,10,20,50]]
segments.append(10000)

a = 0
b = 10.0 # s
print("Numerical Integration based on the book NUMERICAL METHODS FOR ENGINEERS 8th Edition")
print("-----------------------------------------------------------------------------------")
print("Trapezoidal rule, Simpson's 1/3 rule and Simpson's 3/8 rule adapted from pseudocode on page 632")
print("Applied on Example 21.3 on page 622 and 623")
print("\nThe velocity of a falling object with air resistance where g is acceleration due to gravity, m is mass\nc is the drag coefficient, t is time:")
print("Velocity: v(t) = g * m / c * (1 - exp(-(c * t / m))")
print("\nDistance D is found by integrating v(t)")
print("\nWhat is distance at t=10s ? for given mass m = 68.1kg and drag coeff. c = 12.5 kg/s")
print(f"Exact answer obtained using calculus is D = {distance_exact}m")
print()
print("                           Trapezoidal rule          Simpson's 1/3 rule          Simpson's 3/8 rule")
print("Segments | Segment size|D (m)       |et(%)       |D (m)       |et(%)       |n mod    |D (m)       |et(%)      ")
for n in segments:
    distance_trap, h = trapm(a, b , n, velocity)
    distance_simpson13, h = simpsons13m(a, b , n, velocity)
    distance_simpson38, h, n_mod = simpsons38m(a, b , n, velocity)
    error_trap = 100 * (distance_trap - distance_exact) / distance_exact
    error_simpson13 = 100 * (distance_simpson13 - distance_exact) / distance_exact
    error_simpson38 = 100 * (distance_simpson38 - distance_exact) / distance_exact
    print(f"{n:>9}|{h:>13.1e}|{distance_trap:>12.6f}|{error_trap:>11.2}%|", end = "")
    print(f"{distance_simpson13:>12.6f}|{error_simpson13:>11.2}%|", end = "")
    print(f"{n_mod:>9}|{distance_simpson38:>12.6f}|{error_simpson38:>11.2}%")
