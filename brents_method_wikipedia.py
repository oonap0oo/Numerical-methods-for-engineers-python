# Brent's Method for root finding
# adapted from wikipedia pseudocode
# on https://en.wikipedia.org/wiki/Brent%27s_method#Algorithm

from math import *

def brents_wiki(f, interval):
    """Brent's Method
       Adapted from wikipedia pseudocode
       fun: function to find root of
       interval: iterable of two x values which bracket the root"""
    print("Brent's Method for root finding")
    epsilon = 2**-52
    tol = 2*epsilon
    a, b = interval
    fa=f(a); fb=f(b)
    if fa * fb >= 0:
        print("Root is not bracketed")
        return
    if abs(fa) < abs(fb):
        a,b = b,a
        fa,fb = fb,fa
    c = a
    fc = f(c)
    fs = fb
    mflag = True
    counter = 1
    while not (fs == 0 or abs(b - a) <= tol):
        if fa != fc and fb != fc: # inverse quadratic interpolation
            s  = a*fb*fc / ((fa-fb)*(fa-fc))
            s += b*fa*fc / ((fb-fa)*(fb-fc))
            s += c*fa*fb / ((fc-fa)*(fc-fb))
            msg = "inverse quadratic interpolation"
        else: # secant method
            s = b - fb * (b-a) / (fb - fa)
            msg = "secant method"
        s_range = sorted([(3*a+b)/4, b]) # the limit (3*a+b)/4 can be greater or smaller then the other limit b
        condition1 = s < s_range[0] or s > s_range[1] # define 5 conditions, if 1 is True bisection mathod has to be used
        condition2 = mflag == True and abs(s-b) >= abs(b-c)/2
        condition3 = mflag == False and abs(s-b) >= abs(c-d)/2
        condition4 = mflag == True and abs(b-c) < epsilon
        condition5 = mflag == False and abs(c-d) < epsilon
        if condition1 or condition2 or condition3 or condition4 or condition5:
            s = (a+b)/2 # bisection method
            msg = "bisection method"
            mflag = True
        else:
            mflag = False
        fs = f(s)
        d = c # d is assigned for the first time here
        c = b
        fc = fb
        if fa*fs < 0:
            b = s
            fb = fs
        else:
            a = s
            fa = fs
        if abs(fa) < abs(fb):
            a,b = b,a
            fa,fb = fb,fa
        tol = 2 * epsilon * max(abs(s) ,1)
        print(f"{counter}:{msg:<30}\ts = {s}")
        counter += 1
    return s


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
friction_factor = brents_wiki(Colebrook_eq, interval)
print("\nResult for friction factor f:")
print(f"f = {friction_factor}")
print(f"Residual: Colebrook equation(f) = {Colebrook_eq(friction_factor)}")
        

