# Bisection method
# Adapted from NUMERICAL METHODS FOR ENGINEERS 8th Edition
# Pseudocode demonstrating Bisection method on page 135

from math import *

def bisect(f, interval, imax, es):
    """Bisection method
    f: function of one argumant to find root of
    interval: iterable with lowel and upper guess (xl,xu)
    imax: max allowed number of iterations
    es: maximum relative error allowed in %
    """
    xl, xu = interval # lower and upper guesses
    fl = f(xl)
    iter_ = 0
    xr = xu
    while True:
        xr_old = xr # save previous root estimation
        xr = (xl + xu) / 2 # new estimate for root
        fr = f(xr) # function value at new root estimate, only 1 call to f() per iteration
        iter_ += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100 # relative error estimate in %
        test = fl * fr
        if test < 0: # values of function at xr and xl have different signs
            xu = xr # root must be in lower half of interval, fu=f(xu) is never used so no need to update
        elif test > 0: # values of function at xr and xl have same signs
            xl = xr # root must be in upper half of interval
            fl = fr # update fl value here only when xl changes without recalculating from f()
        else:
            ea = 0 # fr must be zero, then xr is root
        if ea < es or iter_ >= imax: # rel error small enough or max iter reached
            break
    return xr, iter_, ea


def fun(x):
    """Function to find root of
        f(x) = sin(2*pi*x) + exp(-x)"""
    return sin(2*pi*x) + exp(-x)

interval = (0.5, 0.8)
result, steps, rel_error = bisect(fun ,interval ,50 , 0.01)
print(fun.__doc__)
print("Interval for root:",interval)
print(f"root xr = {result} +-{rel_error:.1}%")
print(f"residual f(xr) = {fun(result):.3}")
print("number of steps", steps)
