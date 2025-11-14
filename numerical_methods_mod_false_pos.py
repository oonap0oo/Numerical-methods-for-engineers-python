# Modified False position method
# Adapted from NUMERICAL METHODS FOR ENGINEERS 8th Edition
# adapted from pseudocode on page 141

from math import *

def modfalsepos(f, interval, imax, es):
    """Modified false position method
    f: function of one argument to find root of
    interval: iterable with lowel and upper guess (xl,xu)
    imax: max allowed number of iterations
    es: maximum relative error allowed in %
    """
    xl, xu = interval # lower and upper guesses
    iter_ = 0
    fl = f(xl)
    fu = f(xu)
    xr = xu
    iu = 0; il = 0
    while True:
        xr_old = xr # save previous root estimation
        xr = xu - fu * (xl - xu) / (fl - fu) # new estimate for root
        fr = f(xr) # function value at new root estimate
        iter_ += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100 # relative error estimate in %
        test = fl * fr
        if test < 0: # values of function at xr and xl have different signs
            xu = xr # root must be in lower half of interval
            fu = f(xu)
            iu = 0
            il += 1
            if il >= 2:
                fl /= 2
        elif test > 0: # values of function at xr and xl have same signs
            xl = xr # root must be in upper half of interval
            fl = f(xl)
            il = 0
            iu += 1
            if iu >=2:
                fu /= 2
        else:
            ea = 0 # fr must be zero, then xr is root
        if ea < es or iter_ >= imax: # rel error small enough or max iter reached
            break
    return xr, iter_, ea


def standardfalsepos(f, interval, imax, es):
    """Standard false position method
    f: function of one argument to find root of
    interval: iterable with lowel and upper guess (xl,xu)
    imax: max allowed number of iterations
    es: maximum relative error allowed in %
    """
    xl, xu = interval # lower and upper guesses
    iter_ = 0
    fl = f(xl)
    fu = f(xu)
    xr = xu
    while True:
        xr_old = xr # save previous root estimation
        xr = xu - fu * (xl - xu) / (fl - fu) # new estimate for root
        fr = f(xr) # function value at new root estimate
        iter_ += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100 # relative error estimate in %
        test = fl * fr
        if test < 0: # values of function at xr and xl have different signs
            xu = xr # root must be in lower half of interval
            fu = f(xu)
        elif test > 0: # values of function at xr and xl have same signs
            xl = xr # root must be in upper half of interval
            fl = f(xl)
        else:
            ea = 0 # fr must be zero, then xr is root
        if ea < es or iter_ >= imax: # rel error small enough or max iter reached
            break
    return xr, iter_, ea



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


# Example 5.6 page 139
# xr**10 - 1 = 0
# xr = 1.0
def fun(x):
    """f(x) = x**10 - 1 = 0"""
    return x**10 - 1

interval = (0, 1.3)
error_percent = 0.01
N = 100

result, steps, rel_error = bisect(fun, interval, N, error_percent)
print("Bisection method")
print(fun.__doc__)
print("Interval for root:",interval)
print(f"root xr = {result} +-{rel_error:.1}%")
print(f"residual f(xr) = {fun(result):.3}")
print("number of steps", steps)

result, steps, rel_error = standardfalsepos(fun, interval, N, error_percent)
print("\nStandard false position method")
print(fun.__doc__)
print("Interval for root:",interval)
print(f"root xr = {result} +-{rel_error:.1}%")
print(f"residual f(xr) = {fun(result):.3}")
print("number of steps", steps)


result, steps, rel_error = modfalsepos(fun, interval, N, error_percent)
print("\nModified false position method")
print(fun.__doc__)
print("Interval for root:",interval)
print(f"root xr = {result} +-{rel_error:.1}%")
print(f"residual f(xr) = {fun(result):.3}")
print("number of steps", steps)


