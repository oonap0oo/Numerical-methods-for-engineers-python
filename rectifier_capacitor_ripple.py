info = r"""Example of application Numerical methods for equation root finding
------------------------------------------------------------------
The mains voltage is rectified using 4 diodes in bridge configuration. The resulting d.c. voltage is smoothed suing a capacitor with value C When the rectifier is loaded with resistance R what is the remaining ripple of the reftified d.c. voltage?

~ o--+---->|-------+-----+--------+ Vp
     |             |     |        |
     +----|<----+  |     |        \
                |  |    ---       /
                |  |    --- C     \ R
     +---->|-------+     |        /
     |          |        |        |
~ o-------|<----+--------+--------+ 0V

voltage at anode of a diode:
va(t) = -Vamplitude*cos(2*pi*f*t)

voltage on capacitor:
vc(t) = Vamplitude*exp(-t/(R*C))

voltage on capacitor drops until next pair of diodes conduct, ignoring diode forward voltage:
va(t1) = vc(t1)
-Vamplitude*cos(2*pi*f*t1) = Vamplitude*exp(-t1/(R*C))
exp(-t1/(R*C)) + cos(2*pi*f*t1) = 0"""

from math import *


def f(t):
    """exp(-t1/(R*C)) + cos(2*pi*f*t1) = 0"""
    return exp(-t/(R*C)) + cos(2*pi*f_mains*t)

def v(t):
    """Vamplitude*exp(-t1/(R*C))"""
    return Vamplitude*exp(-t1/(R*C))


def bisect(f, interval, imax, es):
    """Bisection method
    f: function of one argument to find root of
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
        #print(f"{iter_}: xl = {xl:<10.6e} xu = {xu:<10.6e}")
    return xr, iter_, ea



# circuit parameters
Vrms = 230 # Volt
Vamplitude = sqrt(2)*Vrms
R = 5E3 # Ohm
C = 220E-6 # Farad
f_mains = 50 # Hertz

# numerical parameters
t0 = 0.0 # intial guesses for t
t1 = 10E-3
es = 0.01 # max. relative error in %
imax = 100 # max. number of iterations

# find root and display result
print(info)
print("\nUsing Bisection Method")
print(f"Finding root of {f.__doc__} which will give time tr\nwhen voltage on capacitor is lowest")
print(f"Initial guesses for t: t0 = {t0}, t1 = {t1}")
root, steps, rel_error = bisect(f, (t0, t1), imax, es)

if root != None:
    print(f"\nFound tr = {root:10.8e} +-{rel_error:.1}% after {steps} iterations, Residual: f(tr) = {f(root):.3}")
    print(f"Mains voltage: {Vrms}V at {f_mains} Hz, With smoothing capacitor C = {C:.1e}F, load resistance R = {R}Ohm")
    vmin = v(root)
    print(f"Lowest voltage on capacitor at t={root:10.3e}s = {vmin:.3f}V")
    print(f"Mains voltage of {Vrms}Vrms, Amplitude of mains voltage is also highest voltage on capacitor: {Vamplitude:.3f}V")
    vripple = Vamplitude - vmin
    print(f"Ripple voltage: Vripple = {Vamplitude:.3f}V - {vmin:.3f}V = {vripple:.3f}Vpp")
else:
    print(f"No root found after {steps} iterations")
