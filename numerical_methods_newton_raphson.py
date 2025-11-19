# Newton-Raphson method
# Adapted from NUMERICAL METHODS FOR ENGINEERS 8th Edition
# adapted from pseudocode on page 153, info on page 157

# df(xn)/dt = f(xn) / (xn  - xn+1)
# xn - xn+1 = f(xn) / df(xn)/dt
# xn+1 = xn - f(xn) / df(xn)/dt

from math import *

def newton_raphson(f, Df, x0, es, imax):
    """Newton-Raphson method
       f: function to find root of
       Df: derivative function of f
       x0: initial guess for root
       es: max. percentage error
       imax: max. number iterations"""
    xr = x0
    for iter_ in range(imax): 
        xr_old = xr
        df_dt = Df(xr_old)
        if df_dt != 0:
            xr = xr_old - f(xr_old) / df_dt
        else:
            xr = None; ea = None
            break
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        print(f"x{iter_} = {xr:.8f}, ea = {ea:.4}%")
        if ea < es:
            break
    return xr, iter_+1, ea


def report(f, method, result):
    root, steps, rel_error = result
    if root != None:
        print("\nNewton-Raphson method")
        print(f.__doc__)
        print("Initial guess for root:",x_init)
        print(f"root xr = {root} +-{rel_error:.1}%")
        print(f"residual f(xr) = {f(root):.3}")
        print("number of steps", steps)
    else:
        print(f"Derivative equal to zero after {steps} iterations")


def f(x):
    """f(x) = exp(-x) - x = 0"""
    return  exp(-x) - x

def Df(x):
    """df/dt"""
    return -exp(-x) - 1

x_init = 0
es = 0.1
imax = 100

result = newton_raphson(f, Df, x_init, es, imax)
report(f, newton_raphson, result)


