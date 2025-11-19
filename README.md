# Numerical Methods For Engineers - Python
Python versions of some of the example pseudocode in the book "Numerical methods for engineers 8th edition". Unless mentioned the code only uses libraries which come with a CPython installation such as math.

## Roots of equations

### Modified False position method
Adapted from pseudocode on page 141

Comparing bisection, false position and modified false position on an given example

[numerical_methods_mod_false_pos.py](numerical_methods_mod_false_pos.py)

### Incremental search for sign changes and modified false position method

As described in NUMERICAL METHODS FOR ENGINEERS  8th Edition

Incremental search for sign changes of function adapted from pseudocode on page 142

combined with modified false position root finding method adapted from pseudocode on page 141

This code allows the user to enter a function of x and a interval on the x-axis.

The interval is searched for sign changes, these points are furhter refined yielding the roots using modfified false position.

![numerical_methods_incremental_search_false_pos_screenshot.png](numerical_methods_incremental_search_false_pos_screenshot.png)

code: [numerical_methods_incremental_search_false_pos_3.py](numerical_methods_incremental_search_false_pos_3.py)

A second version also generates a plot using the matplotlib library

![numerical_methods_incremental_search_false_pos_plot_screenshot.png](numerical_methods_incremental_search_false_pos_plot_screenshot.png)

code: [numerical_methods_incremental_search_false_pos_plot.py](numerical_methods_incremental_search_false_pos_plot.py)

### Newton-Raphson method

Adapted from NUMERICAL METHODS FOR ENGINEERS 8th Edition from pseudocode on page 153, info on page 157

This method uses both f(x) and the derivative function f'(x) to approximate the root

    xn+1 = xn - f(xn) / df(xn)/dt

code: [numerical_methods_newton_raphson.py](numerical_methods_newton_raphson.py)

### Secant method

Using info out of NUMERICAL METHODS FOR ENGINEERS 8th Edition on page 158

The deivative of function f(x) is approximated by

    df(xn)/dt ≈ (f(xn-1)- f(xn) / (xn-1 - xn)

code: [numerical_methods_secant.py](numerical_methods_secant.py)

### Mofidied secant method

Using info out of NUMERICAL METHODS FOR ENGINEERS 8th Edition on page 162

This variant uses a fractional change ε (epsilon) of the independant variable x to prroximate the derivative of f(x)

    df(xn)/dt ≈ ( (f(xn + epsilon*xn) - f(xn) ) / (epsilon*xn)

code: [numerical_methods_modified_secant.py](numerical_methods_modified_secant.py)

