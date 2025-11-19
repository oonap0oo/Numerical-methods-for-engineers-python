# Secant method
# Using info out of NUMERICAL METHODS FOR ENGINEERS 8th Edition on page 158

# Newton Raphson uses derivative of function f:
# df(xn)/dt = f(xn) / (xn  - xn+1)
# xn - xn+1 = f(xn) / df(xn)/dt
# xn+1 = xn - f(xn) / df(xn)/dt

# Secant method approximated derivative value:
# df(xn)/dt ≈ (f(xn-1)- f(xn) / (xn-1 - xn)

# Using approximation of derivative in Newton Raphson:
# xn+1 = xn - f(xn) * (xn-1 - xn) / (f(xn-1)- f(xn))

# Modified secant method
# df(xn)/dt ≈ ( (f(xn + epsilon*xn) - f(xn) ) / (epsilon*xn)

# xn+1 = xn - f(xn) * (epsilon*xn) / (f(xn + epsilon*xn) - f(xn))


from math import *

def secant_mod(f, x0, epsilon, es, imax):
    """Modified secant method
       f: function to find root of
       x0: initial guess of root
       epsilon: small factor, dx is approximated by epsilon*x
       es: maximum allowed percentage error
       imax: maximum number iterations"""
    for iter_ in range(imax):
        f0 = f(x0)
        f1 = f(x0 + epsilon * x0)
        if f1 != f0:
            x1 = x0 - f0 * (epsilon * x0) / (f1 - f0)
        else:
            x1 = None; ea = None
            break
        if x1 != 0:
            ea = abs((x1 - x0) / x1) * 100
        print(f"step {iter_+1}: x{iter_+2} = {x1:.8f}, ea = {ea:.4}%")
        if ea < es:
            break
        x0 = x1
    return x1, iter_+1, ea


def report(f, method, result):
    root, steps, rel_error =result
    if root != None:
        print("\nRoot of " + f.__doc__)
        print("Using Modified secant method")
        print(f"Initial guesses for root: x0 = {x0}, epsilon = {epsilon}")
        print(f"root xr = {root} +-{rel_error:.1}%")
        print(f"residual f(xr) = {f(root):.3}")
        print(f"{steps} iterations)")
    else:
        print(f"No root found after {steps} iterations")


def f(x):
    """f(x) = exp(-x) - x = 0"""
    return  exp(-x) - x

x0 = 1.0 # intial guesses for root
epsilon = 0.01
es = 0.01 # max. relative error in %
imax = 100 # max. number of iterations

result = secant_mod(f, x0, epsilon, es, imax)
report(f, secant_mod, result)


