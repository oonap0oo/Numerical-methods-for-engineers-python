# Brent's Method
# Adapted from NUMERICAL METHODS FOR ENGINEERS 8th Edition
# Pseudocode demonstrating Brent's method on page 166
# Applied on Case Study 8.4 Pipe Friction

from math import *

def brents(fun, interval):
    """Brent's Method
       fun: function to find root of
       interval: iterable of two x values which bracket the root"""
    print("Brent's Method for root finding")
    # machine epsilon for a standard 64 bit double float = 2**-52
    # Machine Epsilon describes the round-off error for a floating-point number with a certain amount of precision.
    # It is the upper bound on the relative approximated error caused due to rounding off floating numbers.
    # It is also defined as the gap between the number 1 and the next largest floating point number
    epsilon = 2.220446049250313E-16
    #tol = 1E-6
    xl, xu = interval
    a = xl; b = xu; fa = fun(a); fb = fun(b) # a,b,c define the search interval
    c = a; fc = fa; d = b - c; e = d
    counter = 1
    while True:
        if fb == 0:
            break
        if copysign(1 ,fa) == copysign(1, fb):
            # if necessary rearange points
            a = c; fa = fc; d = b - c; e = d
        if abs(fa) < abs(fb):
            c = b; b = a; a = c
            fc = fb; fb = fa; fa = fc
        m = 0.5 * (a - b) # Termination test end possible exit
        tol = 2 * epsilon * max(abs(b) ,1) # tol is two times machine epsilon times |b| if |b| is greater then 1
        if abs(m) <= tol or fb == 0:
            break
        # Choose open method or bisection
        if abs(e) >= tol and abs(fc) > abs(fb): # open method
            s = fb / fc
            if a == c: # *** Secant method ****
                print(f"{counter}: Secant method  b={b:.12}")
                p = 2 * m * s
                q = 1 - s
            else: # *** inverse quadratic interpolation ***
                print(f"{counter}: Inverse quadratic interpolation  b={b:.12}")
                q = fc / fa; r = fb / fa
                p = s * ( 2 * m * q * (q - r)   -   (b - c) * (r - 1) )
                q = (q - 1) * (r - 1) * (s - 1)
            if p > 0:
                q = -q
            else:
                p = -p
            if 2 * p < 3 * m * q - abs(tol * q) and p < abs(0.5 * e * q):
                e = d; d = p / q
            else:
                d = m; e = m
        else: # *** Bisection ***
            print(f"{counter}: Bisection  b={b:.12}")
            d = m; e = m
        c = b; fc = fb
        if abs(d) > tol:
            b = b + d
        else:
            b = b - copysign(tol ,b - a)
        fb = fun(b)
        counter += 1
    return b 


def Colebrook_eq(f):
    """Function to find root of
       Colebrook equation 
       Out of Case study 8.4 Pipe Friction"""
    # f: Friction factor range from 0.008 to 0.08
    return 1/sqrt(f) + 2 * log10( eps/(3.7*D) + 2.51/(Re*sqrt(f)) )

# parameters Colebrook equation
rho = 1.23 # kg/m³ fluid density
mu = 1.79E-5 # N.s/m² dynamic viscosity
D = 0.005 # m Diameter
V = 40 # m/s fluid velocity
eps = 0.0015E-3 # m Roughness
Re = rho*V*D/mu # Reynolds number
#Re = 13743
# f: Friction factor range from 0.008 to 0.08
interval = (0.008, 0.08)



print("Case Study 8.4 Pipe Friction")
print("----------------------------")
print("Finding friction factor f using Colebrook equation:")
print("-1/sqrt(f) = 2 * log10( eps/(3.7*D) + 2.51/(Re*sqrt(f)) )")
print("By appying Brent's method for root finding on:")
print("1/sqrt(f) + 2 * log10( eps/(3.7*D) + 2.51/(Re*sqrt(f)) ) = 0")
print(f"Reynolds number: Re={Re}")
print(f"Roughness: epsilon={eps}m")
print(f"Diameter: D={D}m\n")
friction_factor = brents(Colebrook_eq, interval)
print("\nResult for friction factor f:")
print(f"f = {friction_factor}")
print(f"Residual: Colebrook equation(f) = {Colebrook_eq(friction_factor)}")
        

    
